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
    "cure_*"
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

ELEMENTAL_CHAR_KEYS = {
    "dark": "(D)",
    "light": "(L)",
    "earth": "(Ë)",
    "fire": "(F)",
    "water": "(W)",
    "air": "(A)",
    "ice": "(I)",
    "electric": "(É)",
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
        "duration_per_level":-1,
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
# Single canonical source for the unicode glyphs used to render status effects
# (buffs/debuffs/afflictions) and elemental affinities in compact columns such
# as the ability-handler "Statuses" column and the monster-log detail panel.
STATUS_SYMBOLS = {
    "all":                    "☯",
    "petrify":                "⬡",
    "stun":                   "✦",
    "sleep":                  "☽",
    "confuse":                "⁈",
    "silence":                "⊘",
    "continuous_damage":      "♾",
    "regen":                  "♻",
    "elemental_debuff":       "◆",
    "attack_debuff":          "↓A",
    "defense_debuff":         "↓D",
    "strength_debuff":        "↓S",
    "dexterity_debuff":       "↓X",
    "intelligence_debuff":    "↓I",
    "constitution_debuff":    "↓C",
    "attack_buff":            "↑A",
    "defense_buff":           "↑D",
    "strength_buff":          "↑S",
    "dexterity_buff":         "↑X",
    "intelligence_buff":      "↑I",
    "constitution_buff":      "↑C",
    "elemental_attack_buff":  "↑EA",
    "elemental_defense_buff": "↑ED",
    "scanned":                "👁",
}


def fmt_element_glyphs(elems) -> str:
    """Format a list of element names as compact glyphs (e.g. '(D)(L)').

    Uses ELEMENTAL_CHAR_KEYS as the canonical element glyph map; unknown
    elements fall back to a parenthesized first letter. Returns '—' when empty.
    """
    if not elems:
        return "—"
    return "".join(
        ELEMENTAL_CHAR_KEYS.get(e, f"({e[:1].upper()})") for e in elems
    )


def fmt_status_glyphs(statuses) -> str:
    """Format a list of status ids as compact unicode glyphs separated by spaces.

    Unknown ids fall back to a bracketed two-letter abbreviation. Returns '—'
    when empty.
    """
    if not statuses:
        return "—"
    return " ".join(
        STATUS_SYMBOLS.get(s, f"[{s[:2]}]") for s in statuses
    )