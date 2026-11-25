"""
Shared constants and Rich styles used across multiple handler modules.
"""
from __future__ import annotations

from rich.style import Style

from game.constants_other import (
    ELEMENT_SYMBOLS,
    ELEMENTAL_COLORS,
    STATUS_SYMBOLS,
    STATUS_COLORS,
    fmt_status_glyphs,
)

# ── Category name constants ────────────────────────────────────────────────────

DIALOG_CATEGORY       = "character_dialog"
EQUIPMENT_CATEGORY    = "equipment"
TIMELINE_CATEGORY     = "timeline"
NPC_CATEGORY          = "npc"
ABILITY_CATEGORY      = "ability"
HOSTILE_CATEGORY      = "hostile"
DUNGEON_CATEGORY      = "dungeon"
CITY_CATEGORY         = "city"
CHARACTER_CATEGORY    = "character"
SIMULATION_CATEGORY   = "simulation"
SPECIAL_ITEM_CATEGORY = "special_item"
LOAD_SAVE_CATEGORY    = "load_save"

# ── Shared row styles ──────────────────────────────────────────────────────────

ROW_ERROR_STYLE   = Style(color="red")
ROW_WARN_STYLE    = Style(color="yellow")
ROW_NOTICE_STYLE  = Style(color="#e040fb")   # magenta
ROW_BLUE_STYLE    = Style(color="#2323ff")   # blue — balance strong / ability strong
ROW_INFO_STYLE    = Style(color="cyan")      # balance weak / info
ROW_OK_STYLE      = Style(color="green", dim=True)
ROW_DEFAULT_STYLE = Style()

# ── Shared symbol maps ────────────────────────────────────────────────────────
# ELEMENT_SYMBOLS / STATUS_SYMBOLS (and their *_COLORS counterparts) are
# imported from game.constants_other, the single canonical source, so glyphs
# never drift out of sync across the dev tools, equip overlay, and shop menu.


def fmt_elem_list(elems: list[str]) -> str:
    """Format a list of element names as compact symbols."""
    if not elems:
        return "—"
    return "".join(ELEMENT_SYMBOLS.get(e, f"({e[:1].upper()})") for e in elems)


def fmt_status_list(statuses: list[str]) -> str:
    """Format a list of status ids as symbol+3-letter-id, e.g. '↑ATK ↓DEF'.

    Retains the full fmt_status_glyphs() id suffix (rather than a bare icon)
    so the dev ability table can distinguish stat buffs/debuffs that would
    otherwise share the same arrow symbol.
    """
    if not statuses:
        return "—"
    return fmt_status_glyphs(statuses)