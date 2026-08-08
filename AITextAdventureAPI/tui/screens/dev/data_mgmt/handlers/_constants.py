"""
Shared constants and Rich styles used across multiple handler modules.
"""
from __future__ import annotations

from rich.style import Style

# ── Category name constants ────────────────────────────────────────────────────

DIALOG_CATEGORY      = "character_dialog"
EQUIPMENT_CATEGORY   = "equipment"
TIMELINE_CATEGORY    = "timeline"
NPC_CATEGORY         = "npc"
ABILITY_CATEGORY     = "ability"
HOSTILE_CATEGORY     = "hostile"
DUNGEON_CATEGORY     = "dungeon"
CITY_CATEGORY        = "city"
CHARACTER_CATEGORY   = "character"
SIMULATION_CATEGORY  = "simulation"

# ── Shared row styles ──────────────────────────────────────────────────────────

ROW_ERROR_STYLE   = Style(color="red")
ROW_WARN_STYLE    = Style(color="yellow")
ROW_NOTICE_STYLE  = Style(color="#e040fb")   # magenta
ROW_BLUE_STYLE    = Style(color="#2323ff")   # blue — balance strong / ability strong
ROW_INFO_STYLE    = Style(color="cyan")      # balance weak / info
ROW_OK_STYLE      = Style(color="green", dim=True)
ROW_DEFAULT_STYLE = Style()

# ── Shared symbol maps ────────────────────────────────────────────────────────

ELEMENT_SYMBOLS: dict[str, str] = {
    "dark":     "(D)",
    "light":    "(L)",
    "earth":    "(Ë)",
    "fire":     "(F)",
    "water":    "(W)",
    "air":      "(A)",
    "ice":      "(I)",
    "electric": "(É)",
}

STATUS_SYMBOLS: dict[str, str] = {
    "petrify":               "⬡",
    "stun":                  "✦",
    "sleep":                 "☽",
    "confuse":               "⁈",
    "silence":               "⊘",
    "continuous_damage":     "♾",
    "elemental_debuff":      "◆",
    "attack_debuff":         "↓A",
    "defense_debuff":        "↓D",
    "strength_debuff":       "↓S",
    "dexterity_debuff":      "↓X",
    "intelligence_debuff":   "↓I",
    "constitution_debuff":   "↓C",
    "attack_buff":           "↑A",
    "defense_buff":          "↑D",
    "strength_buff":         "↑S",
    "dexterity_buff":        "↑X",
    "intelligence_buff":     "↑I",
    "constitution_buff":     "↑C",
    "elemental_attack_buff": "↑EA",
    "elemental_defense_buff":"↑ED",
    "scanned":               "👁",
}


def fmt_elem_list(elems: list[str]) -> str:
    """Format a list of element names as compact symbols."""
    if not elems:
        return "—"
    return "".join(ELEMENT_SYMBOLS.get(e, f"({e[:1].upper()})") for e in elems)


def fmt_status_list(statuses: list[str]) -> str:
    """Format a list of status ids as compact unicode glyphs."""
    if not statuses:
        return "—"
    return " ".join(STATUS_SYMBOLS.get(s, f"[{s[:2]}]") for s in statuses)