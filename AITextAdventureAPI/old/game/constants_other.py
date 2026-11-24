# PLAYER ABILITY SEED DATA
# Abilities are split into per-level seed modules under region_seeds/player_abilities.
# Import level-specific lists if available and compose PLAYER_ABILITY_SEEDS from them.
from game.region_seeds.player_abilities.level_1_abilities import LEVEL_1_PLAYER_ABILITY_SEEDS
from game.region_seeds.player_abilities.level_2_abilities import LEVEL_2_PLAYER_ABILITY_SEEDS
from game.region_seeds.player_abilities.level_3_abilities import LEVEL_3_PLAYER_ABILITY_SEEDS
from game.region_seeds.player_abilities.level_4_abilities import LEVEL_4_PLAYER_ABILITY_SEEDS
from game.region_seeds.player_abilities.level_5_abilities import LEVEL_5_PLAYER_ABILITY_SEEDS
from game.region_seeds.player_abilities.unique_character_abilities import UNIQUE_CHARACTER_ABILITY_SEEDS

# Compose final PLAYER_ABILITY_SEEDS from per-level lists and the remaining inline list
PLAYER_ABILITY_SEEDS = []
PLAYER_ABILITY_SEEDS.extend(LEVEL_1_PLAYER_ABILITY_SEEDS)
PLAYER_ABILITY_SEEDS.extend(LEVEL_2_PLAYER_ABILITY_SEEDS)
PLAYER_ABILITY_SEEDS.extend(LEVEL_3_PLAYER_ABILITY_SEEDS)
PLAYER_ABILITY_SEEDS.extend(LEVEL_4_PLAYER_ABILITY_SEEDS)
PLAYER_ABILITY_SEEDS.extend(LEVEL_5_PLAYER_ABILITY_SEEDS)
PLAYER_ABILITY_SEEDS.extend(UNIQUE_CHARACTER_ABILITY_SEEDS)

# sort by level so module export is ordered
PLAYER_ABILITY_SEEDS.sort(key=lambda s: s.get("level",0))

BENEFICIAL_PLAYER_ABILITY_EFFECTS = [
    "heal",
    "status",
    "*_buff",
    "revive", 
    "cure",
]

HARMFUL_STATUS_EFFECTS = {"elemental_debuff",
                          "attack_debuff",
                          "defense_debuff",
                          "intelligence_debuff",
                          "strength_debuff",
                          "dexterity_debuff",
                          "constitution_debuff",
                          "petrify",
                          "stun",
                          "sleep",
                          "confuse",
                          "silence",
                          "continuous_damage"}

BENEFICIAL_ITEM_EFFECTS = [
    "heal_*",
    "restore_ap_*",
    "cure_*",
    "stat_increase",
]

ABILTITY_EFFECT_DISPLAY_NAME = {
    "damage": "Damage",
    "heal": "Heal",
    "status": "Status",
    "revive": "Revive"
}

ABILITY_STATUS_KEY_DISPLAY_NAMES = {
    "elemental_attack_buff": "E. A. Buff",
    "elemental_defense_buff": "E. D. Buff",
    "attack_buff": "A. Buff",
    "defense_buff": "D. Buff",
    "strength_buff": "Str Buff",
    "dexterity_buff": "Dex Buff",
    "intelligence_buff": "Int Buff",
    "constitution_buff": "Con Buff",
    "elemental_debuff": "E. Debuff",
    "attack_debuff": "A. Debuff",
    "defense_debuff": "D. Debuff",
    "strength_debuff": "Str Debuff",
    "dexterity_debuff": "Dex Debuff",
    "intelligence_debuff": "Int Debuff",
    "constitution_debuff": "Con Debuff",
    "continuous_damage": "Cont Dmg",
    "petrify": "Petrify",
    "sleep": "Sleep",
    "stun": "Stun",
    "confuse": "Confuse",    
    "debuff": "Debuff",
    "scanned": "Scanned",
    "silence": "Silence",
    "regen": "Regen"
}

# ── Element symbols (pure glyph, no letters) ────────────────────────────────
# Use these directly wherever space is tight (list rows, fixed-width columns)
# or when a plain icon is desired without the accompanying 3-letter id.
ELEMENT_SYMBOLS: dict[str, str] = {
    "dark":     "☾",
    "light":    "☀",
    "earth":    "⛰",
    "fire":     "🔥",
    "water":    "💧",
    "air":      "💨",
    "ice":      "❄",
    "electric": "⚡",
    "physical": "✊",
}

# ── Element 3-letter ids ─────────────────────────────────────────────────────
# Paired with ELEMENT_SYMBOLS to build the longer "symbol+id" glyph used in
# detail panels where disambiguation matters more than compactness.
ELEMENTAL_IDS: dict[str, str] = {
    "dark":     "DRK",
    "light":    "LGT",
    "earth":    "EAR",
    "fire":     "FIR",
    "water":    "WTR",
    "air":      "AIR",
    "ice":      "ICE",
    "electric": "ELC",
    "physical": "PHY",
}

# Back-compat combined map (symbol+id) — still used by a couple of dev-tool
# builders that do direct dict lookups rather than calling the formatter
# helpers below. New code should prefer fmt_element_glyphs()/fmt_element_glyphs_rich()
# with the `symbol_only` flag instead of reading this map directly.
ELEMENTAL_CHAR_KEYS: dict[str, str] = {
    key: f"{ELEMENT_SYMBOLS[key]}{ELEMENTAL_IDS[key]}" for key in ELEMENT_SYMBOLS
}

# ── Canonical element colors ─────────────────────────────────────────────────
# Single source of truth for the color associated with each element, used
# anywhere glyphs are rendered with Rich styling (dev tools, equip overlay,
# etc). Kept alongside ELEMENTAL_CHAR_KEYS so both glyph and color stay in
# sync when a new element is added.
ELEMENTAL_COLORS: dict[str, str] = {
    "dark":     "#7c4dff",
    "light":    "#ffee58",
    "earth":    "#8d6e63",
    "fire":     "#ff5252",
    "water":    "#29b6f6",
    "air":      "#b2ebf2",
    "ice":      "#80deea",
    "electric": "#fff176",
    "physical": "#bdbdbd",
}

ELEMENTAL_ADVANTAGE = { # defines the element (value) which is weak to the key
 'light': 'dark',
 'dark': 'light',
 'water': 'fire',
 'fire': 'ice',
 'ice': 'air',
 'air': 'earth',
 'earth': 'electric',
 'electric': 'water'
}


# Element -> status effect templates used by abilities with `effect: "status"`.
# Reworked to be effect-keyed (effect types such as 'elemental_attack_buff',
# 'attack_debuff', 'continuous_damage', etc.). Templates are element-agnostic
# and an applied descriptor will record the element that triggered it.
STATUS_EFFECTS = {
    "elemental_attack_buff": {
        "id": "elemental_attack_buff",
        "display": "E Att Buff",
        "name": "Elemental Attack Buff",
        "type": "elemental attack buff",
        "duration_per_level":2,
        "magnitude_per_level":3,
        "min_magnitude":3,
    },
    "elemental_defense_buff": {
        "id": "elemental_defense_buff",
        "display": "E Def Buff",
        "name": "Elemental Defense Buff",
        "type": "elemental defense buff",
        "duration_per_level":2,
        "magnitude_per_level":3,
        "min_magnitude":3,
    },
    "elemental_debuff": {
        "id": "elemental_debuff",
        "display": "E Debuff",
        "name": "Elemental Debuff",
        "type": "elemental debuff",
        "duration_per_level":2,
        "magnitude_per_level":1,
        "min_magnitude":5,
    },
    "attack_buff": {
        "id": "attack_buff",
        "display": "Attack Buff",
        "name": "Attack Buff",
        "type": "attack buff",
        "duration_per_level":2,
        "magnitude_per_level":4,
        "min_magnitude":2,
    },
    "defense_buff": {
        "id": "defense_buff",
        "display": "Defense Buff",
        "name": "Defense Buff",
        "type": "defense buff",
        "duration_per_level":2,
        "magnitude_per_level":4,
        "min_magnitude":2,
    },
    "attack_debuff": {
        "id": "attack_debuff",
        "display": "Attack Debuff",
        "name": "Attack Debuff",
        "type": "attack debuff",
        "duration_per_level":2,
        "magnitude_per_level":4,
        "min_magnitude":2,
    },
    "defense_debuff": {
        "id": "defense_debuff",
        "display": "Defense Debuff",
        "name": "Defense Debuff",
        "type": "defense debuff",
        "duration_per_level":2,
        "magnitude_per_level":4,
        "min_magnitude":2,
    },
    "strength_buff": {
        "id": "strength_buff",
        "display": "Str Buff",
        "name": "Strength Buff",
        "type": "strength buff",
        "duration_per_level":2,
        "magnitude_per_level":2,
        "min_magnitude":1,
    },
    "strength_debuff": {
        "id": "strength_debuff",
        "display": "Str Debuff",
        "name": "Strength Debuff",
        "type": "strength debuff",
        "duration_per_level":2,
        "magnitude_per_level":2,
        "min_magnitude":1,
    },
    "dexterity_debuff": {
        "id": "dexterity_debuff",
        "display": "Dex Debuff",
        "name": "Dexterity Debuff",
        "type": "dexterity debuff",
        "duration_per_level":2,
        "magnitude_per_level":2,
        "min_magnitude":1,
    },
    "dexterity_buff": {
        "id": "dexterity_buff",
        "display": "Dex Buff",
        "name": "Dexterity Buff",
        "type": "dexterity buff",
        "duration_per_level":2,
        "magnitude_per_level":2,
        "min_magnitude":1,
    },
    "intelligence_buff": {
        "id": "intelligence_buff",
        "display": "Int Buff",
        "name": "Intelligence Buff",
        "type": "intelligence buff",
        "duration_per_level":2,
        "magnitude_per_level":2,
        "min_magnitude":1,
    },
    "intelligence_debuff": {
        "id": "intelligence_debuff",
        "display": "Int Debuff",
        "name": "Intelligence Debuff",
        "type": "intelligence debuff",
        "duration_per_level":2,
        "magnitude_per_level":2,
        "min_magnitude":1,
    },
    "constitution_buff": {
        "id": "constitution_buff",
        "display": "Con Buff",
        "name": "Constitution Buff",
        "type": "constitution buff",
        "duration_per_level":2,
        "magnitude_per_level":2,
        "min_magnitude":1,
    },
    "constitution_debuff": {
        "id": "constitution_debuff",
        "display": "Con Debuff",
        "name": "Constitution Debuff",
        "type": "constitution debuff",
        "duration_per_level":2,
        "magnitude_per_level":2,
        "min_magnitude":1,
    },
    "continuous_damage": {
        "id": "continuous_damage",
        "display": "Cont Dmg",
        "name": "Continuous Damage",
        "type": "continuous damage",
        "duration_per_level":-1,
        "magnitude_per_level":0.5,
        "min_damage_per_turn":1,
    },
    "petrify": {
        "id": "petrify",
        "display": "Petrify",
        "name": "Petrify",
        "type": "petrify",
        "duration_per_level":-1,
        "magnitude_per_level":0,
    },
    "stun": {
        "id": "stun",
        "display": "Stun",
        "name": "Stun",
        "type": "status",
        "duration_per_level":2,
        "magnitude_per_level":0,
    },
    "sleep": {
        "id": "sleep",
        "display": "Sleep",
        "name": "Sleep",
        "type": "status",
        "duration_per_level":2,
        "magnitude_per_level":0,
    },
    "confuse": {
        "id": "confuse",
        "display": "Confuse",
        "name": "Confuse",
        "type": "status",
        "duration_per_level":2,
        "magnitude_per_level":0,
    },
    "scanned": {
        "id": "scanned",
        "display": "Scanned",
        "name": "Scanned",
        "type": "status",
        "duration_per_level":-1,
        "magnitude_per_level":0,
    },
    "silence": {
        "id": "silence",
        "display": "Silence",
        "name": "Silence",
        "type": "status",
        "duration_per_level":2,
        "magnitude_per_level":0,
    },
    "regen": {
        "id": "regen",
        "display": "Regen",
        "name": "Regeneration",
        "type": "status",
        "duration_per_level":2,
        "magnitude_per_level":0.5,
        "min_heal_per_turn":1,
    },
}

# Generic fallback template when no effect-specific template is found.
GENERIC_STATUS_EFFECT = {
 "id": "generic_status",
 "name": "Status Effect",
 "type": "generic",
 "duration":1,
 "magnitude":1,
}

# ── Compact status / element glyphs ─────────────────────────────────────────
# Pure glyph (no letters) used wherever space is tight (fixed-width columns,
# list rows). Paired with STATUS_IDS below to build the longer "symbol+id"
# form used in detail panels.
STATUS_SYMBOLS: dict[str, str] = {
    "all":                    "☯",
    "petrify":                "⬡",
    "stun":                   "✦",
    "sleep":                  "☽",
    "confuse":                "⁈",
    "silence":                "⊘",
    "continuous_damage":      "♾",
    "regen":                  "♻",
    "elemental_debuff":       "◆",
    "attack_debuff":          "↓",
    "defense_debuff":         "↓",
    "strength_debuff":        "↓",
    "dexterity_debuff":       "↓",
    "intelligence_debuff":    "↓",
    "constitution_debuff":    "↓",
    "attack_buff":            "↑",
    "defense_buff":           "↑",
    "strength_buff":          "↑",
    "dexterity_buff":         "↑",
    "intelligence_buff":      "↑",
    "constitution_buff":      "↑",
    "elemental_attack_buff":  "↑",
    "elemental_defense_buff": "↑",
    "scanned":                "👁",
}

# ── Status 3-letter ids ──────────────────────────────────────────────────────
# Distinguishes which stat/effect a shared symbol (e.g. "↑"/"↓") refers to.
STATUS_IDS: dict[str, str] = {
    "all":                    "ALL",
    "petrify":                "PET",
    "stun":                   "STN",
    "sleep":                  "SLP",
    "confuse":                "CNF",
    "silence":                "SIL",
    "continuous_damage":      "DOT",
    "regen":                  "REG",
    "elemental_debuff":       "ELE",
    "attack_debuff":          "ATK",
    "defense_debuff":         "DEF",
    "strength_debuff":        "STR",
    "dexterity_debuff":       "DEX",
    "intelligence_debuff":    "INT",
    "constitution_debuff":    "CON",
    "attack_buff":            "ATK",
    "defense_buff":           "DEF",
    "strength_buff":          "STR",
    "dexterity_buff":         "DEX",
    "intelligence_buff":      "INT",
    "constitution_buff":      "CON",
    "elemental_attack_buff":  "EAT",
    "elemental_defense_buff": "EDF",
    "scanned":                "SCN",
}

# ── Canonical status colors ──────────────────────────────────────────────────
# Buffs are green-leaning, debuffs/harmful statuses are red/orange-leaning,
# and neutral/utility statuses (scanned) use a cool accent. Single source of
# truth for any Rich-styled status glyph rendering.
STATUS_COLORS: dict[str, str] = {
    "all":                    "#b0bec5",
    "petrify":                "#8d6e63",
    "stun":                   "#ffca28",
    "sleep":                  "#7986cb",
    "confuse":                "#ab47bc",
    "silence":                "#78909c",
    "continuous_damage":      "#e53935",
    "regen":                  "#66bb6a",
    "elemental_debuff":       "#ef5350",
    "attack_debuff":          "#ef5350",
    "defense_debuff":         "#ef5350",
    "strength_debuff":        "#ef5350",
    "dexterity_debuff":       "#ef5350",
    "intelligence_debuff":    "#ef5350",
    "constitution_debuff":    "#ef5350",
    "attack_buff":            "#66bb6a",
    "defense_buff":           "#66bb6a",
    "strength_buff":          "#66bb6a",
    "dexterity_buff":         "#66bb6a",
    "intelligence_buff":      "#66bb6a",
    "constitution_buff":      "#66bb6a",
    "elemental_attack_buff":  "#66bb6a",
    "elemental_defense_buff": "#66bb6a",
    "scanned":                "#29b6f6",
}


def _element_glyph(key: str, symbol_only: bool) -> str:
    symbol = ELEMENT_SYMBOLS.get(key, f"({key[:1].upper()})" if key else "?")
    if symbol_only:
        return symbol
    eid = ELEMENTAL_IDS.get(key, key[:3].upper())
    return f"{symbol}{eid}"


def _status_glyph(key: str, symbol_only: bool) -> str:
    symbol = STATUS_SYMBOLS.get(key, f"[{key[:2]}]" if key else "?")
    if symbol_only:
        return symbol
    sid = STATUS_IDS.get(key, key[:3].upper())
    return f"{symbol}{sid}"


def fmt_element_glyphs(elems, symbol_only: bool = False) -> str:
    """Format a list of element names as compact glyphs.

    By default each element is rendered as "symbol+3-letter-id" (e.g. '🔥FIR').
    Pass symbol_only=True to render just the bare icon (e.g. '🔥') for tight
    spaces such as fixed-width list columns. Unknown elements fall back to a
    parenthesized first letter. Returns '—' when empty.
    """
    if not elems:
        return "—"
    return "".join(
        _element_glyph(str(e).lower(), symbol_only) for e in elems
    )


def fmt_status_glyphs(statuses, symbol_only: bool = False) -> str:
    """Format a list of status ids as compact unicode glyphs separated by spaces.

    By default each status is rendered as "symbol+3-letter-id" (e.g. '↑ATK').
    Pass symbol_only=True to render just the bare icon (e.g. '↑') for tight
    spaces. Unknown ids fall back to a bracketed two-letter abbreviation.
    Returns '—' when empty.
    """
    if not statuses:
        return "—"
    return " ".join(
        _status_glyph(str(s).lower(), symbol_only) for s in statuses
    )


def fmt_element_glyphs_rich(elems, symbol_only: bool = False) -> str:
    """Format a list of element names as Rich-markup colored glyphs.

    Each glyph is wrapped in its canonical color from ELEMENTAL_COLORS, e.g.
    '[#ff5252]🔥FIR[/]'. Pass symbol_only=True to render just the bare colored
    icon (e.g. '[#ff5252]🔥[/]'). Unknown elements fall back to white. Returns
    '—' when empty.
    """
    if not elems:
        return "—"
    out = []
    for e in elems:
        key   = str(e).lower()
        glyph = _element_glyph(key, symbol_only)
        color = ELEMENTAL_COLORS.get(key, "white")
        out.append(f"[{color}]{glyph}[/]")
    return "".join(out)


def fmt_status_glyphs_rich(statuses, symbol_only: bool = False) -> str:
    """Format a list of status ids as Rich-markup colored glyphs, space separated.

    Each glyph is wrapped in its canonical color from STATUS_COLORS. Pass
    symbol_only=True to render just the bare colored icon. Unknown ids fall
    back to white. Returns '—' when empty.
    """
    if not statuses:
        return "—"
    out = []
    for s in statuses:
        key   = str(s).lower()
        glyph = _status_glyph(key, symbol_only)
        color = STATUS_COLORS.get(key, "white")
        out.append(f"[{color}]{glyph}[/]")
    return " ".join(out)