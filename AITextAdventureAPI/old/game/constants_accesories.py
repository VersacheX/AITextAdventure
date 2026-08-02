"""
constants_accessories.py — Accessory seed definitions.

The Accessory dataclass and instantiate_accessory() live in
game.objects.accessory.  This file contains only the seed dicts and
the two public helpers that consume them.

Seed schema:
{
    'id':             str        — unique snake_case identifier
    'name':           str        — display name
    'description':    str        — flavour text + mechanical summary
    'min_level':      int        — minimum player level required to equip
    'rarity':         str        — common | uncommon | rare | superrare | notfound
    'value':          int        — base gold value (sell at 50%)
    'immunities':     list[str]  — status ids blocked entirely
                                   (keys from HARMFUL_STATUS_EFFECTS)
    'resistances':    list[str]  — element names that reduce incoming damage
                                   (keys from ELEMENTAL_ADVANTAGE)
    'weaknesses':     list[str]  — element names that increase incoming damage
    'strength':       int
    'dexterity':      int
    'intelligence':   int
    'constitution':   int
    'crit_bonus':     float      — added to weapon critical_chance (pct pts)
    'damage_bonus':   int        — flat bonus on every outgoing attack
    'special_effect': str        — reserved key for future runtime systems
}
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Any, List, Optional

if TYPE_CHECKING:
    from game.objects.accessory import Accessory


def get_accessory_by_id(accessory_id: str) -> "Optional[Accessory]":
    """Return an instantiated Accessory for the given id, or None."""
    from game.objects.accessory import instantiate_accessory  # noqa: PLC0415
    seed = next((s for s in ACCESSORY_SEEDS if s.get('id') == accessory_id), None)
    return instantiate_accessory(seed) if seed else None


def get_all_accessories() -> "List[Accessory]":
    """Return instantiated Accessory objects for every seed."""
    from game.objects.accessory import instantiate_accessory  # noqa: PLC0415
    return [instantiate_accessory(s) for s in ACCESSORY_SEEDS]


# ── Seed catalogue ─────────────────────────────────────────────────────────────
#
# Level bands mirror the weapon/armor progression:
#   Lv  1-5   common        (starter)
#   Lv  6-10  uncommon      (biome entry)
#   Lv 11-15  rare          (mid-game)
#   Lv 16-20  superrare     (late base-game)
#   Lv 30+    notfound      (attainable-character / end-game tier)

ACCESSORY_SEEDS: List[Dict[str, Any]] = [

    # ── LV 1-5 · COMMON ────────────────────────────────────────────────────

    {
        'id': 'toughened_cord',
        'name': 'Toughened Cord',
        'description': 'A thick braided cord worn around the wrist. Reinforces the body slightly. Resists earth-based impacts.',
        'min_level': 1, 'rarity': 'common', 'value': 60,
        'immunities': [], 'resistances': ['earth'], 'weaknesses': [],
        'strength': 0, 'dexterity': 0, 'intelligence': 0, 'constitution': 2,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'worn_ring',
        'name': 'Worn Ring',
        'description': 'A plain metal ring. Barely magical but noticeably sharpens the senses. Slightly weak to dark energy.',
        'min_level': 1, 'rarity': 'common', 'value': 80,
        'immunities': [], 'resistances': [], 'weaknesses': ['dark'],
        'strength': 1, 'dexterity': 1, 'intelligence': 0, 'constitution': 0,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'lucky_charm',
        'name': 'Lucky Charm',
        'description': 'A trinket carved from river stone. Marginally improves strike timing. Resists water.',
        'min_level': 2, 'rarity': 'common', 'value': 100,
        'immunities': [], 'resistances': ['water'], 'weaknesses': [],
        'strength': 0, 'dexterity': 2, 'intelligence': 0, 'constitution': 0,
        'crit_bonus': 1.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'amber_bead',
        'name': 'Amber Bead',
        'description': 'An amber pendant with a faint warmth. Bolsters mental focus. Resists fire, weak to ice.',
        'min_level': 3, 'rarity': 'common', 'value': 120,
        'immunities': [], 'resistances': ['fire'], 'weaknesses': ['ice'],
        'strength': 0, 'dexterity': 0, 'intelligence': 2, 'constitution': 0,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'refractor_lenses',
        'name': 'Refractor Lenses',
        'description': 'Prismatic lenses that scatter the frequencies used to induce stone-stasis. Grants immunity to Petrify. Resists light.',
        'min_level': 4, 'rarity': 'common', 'value': 200,
        'immunities': ['petrify'], 'resistances': ['light'], 'weaknesses': ['dark'],
        'strength': 0, 'dexterity': 0, 'intelligence': 0, 'constitution': 0,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': '',
    },

    # ── LV 6-10 · UNCOMMON ─────────────────────────────────────────────────

    {
        'id': 'iron_sigil_band',
        'name': 'Iron Sigil Band',
        'description': 'A band stamped with a warding sigil. Disrupts paralysis frequencies. Resists electric, weak to water.',
        'min_level': 6, 'rarity': 'uncommon', 'value': 400,
        'immunities': ['stun'], 'resistances': ['electric'], 'weaknesses': ['water'],
        'strength': 2, 'dexterity': 0, 'intelligence': 0, 'constitution': 1,
        'crit_bonus': 0.0, 'damage_bonus': 1, 'special_effect': '',
    },
    {
        'id': 'soot_wrap',
        'name': 'Soot Wrap',
        'description': 'Alchemical soot-soaked bandages. Keeps the wearer awake through anything. Resists fire, weak to air.',
        'min_level': 6, 'rarity': 'uncommon', 'value': 380,
        'immunities': ['sleep'], 'resistances': ['fire'], 'weaknesses': ['air'],
        'strength': 1, 'dexterity': 1, 'intelligence': 0, 'constitution': 0,
        'crit_bonus': 0.5, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'copper_focus_ring',
        'name': 'Copper Focus Ring',
        'description': 'A finely wound copper ring. Boosts intelligence and crit precision. Resists electric, weak to earth.',
        'min_level': 7, 'rarity': 'uncommon', 'value': 500,
        'immunities': [], 'resistances': ['electric'], 'weaknesses': ['earth'],
        'strength': 0, 'dexterity': 0, 'intelligence': 4, 'constitution': 0,
        'crit_bonus': 1.5, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'sparrow_talon',
        'name': 'Sparrow Talon',
        'description': 'A bird talon on a chain. Improves reaction time. Resists air, weak to ice.',
        'min_level': 8, 'rarity': 'uncommon', 'value': 460,
        'immunities': [], 'resistances': ['air'], 'weaknesses': ['ice'],
        'strength': 0, 'dexterity': 4, 'intelligence': 0, 'constitution': 0,
        'crit_bonus': 2.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'brute_knuckle',
        'name': 'Brute Knuckle',
        'description': 'A weighted knuckle guard that adds raw force to every swing. Resists physical, weak to electric.',
        'min_level': 9, 'rarity': 'uncommon', 'value': 520,
        'immunities': [], 'resistances': ['earth'], 'weaknesses': ['electric'],
        'strength': 4, 'dexterity': 0, 'intelligence': 0, 'constitution': 2,
        'crit_bonus': 0.0, 'damage_bonus': 3, 'special_effect': '',
    },

    # ── LV 11-15 · RARE ────────────────────────────────────────────────────

    {
        'id': 'static_clasp',
        'name': 'Static Clasp',
        'description': 'A clasp crackling with contained discharge. Prevents Stun by grounding voltage. Resists electric, weak to water.',
        'min_level': 11, 'rarity': 'rare', 'value': 1200,
        'immunities': ['stun'], 'resistances': ['electric'], 'weaknesses': ['water'],
        'strength': 0, 'dexterity': 3, 'intelligence': 3, 'constitution': 0,
        'crit_bonus': 1.0, 'damage_bonus': 2, 'special_effect': '',
    },
    {
        'id': 'mind_anchor',
        'name': 'Mind Anchor',
        'description': 'A crystalline pendant that grounds the mind. Grants immunity to Confuse. Resists dark, weak to light.',
        'min_level': 12, 'rarity': 'rare', 'value': 1400,
        'immunities': ['confuse'], 'resistances': ['dark'], 'weaknesses': ['light'],
        'strength': 0, 'dexterity': 0, 'intelligence': 6, 'constitution': 2,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'bloodsteel_amulet',
        'name': 'Bloodsteel Amulet',
        'description': 'Forged from battle-hardened steel soaked in blood ore. Adds bulk and striking power. Resists fire, weak to ice.',
        'min_level': 13, 'rarity': 'rare', 'value': 1600,
        'immunities': [], 'resistances': ['fire'], 'weaknesses': ['ice'],
        'strength': 6, 'dexterity': 0, 'intelligence': 0, 'constitution': 4,
        'crit_bonus': 0.0, 'damage_bonus': 5, 'special_effect': '',
    },
    {
        'id': 'silence_ward',
        'name': 'Silence Ward',
        'description': 'A rune-etched disk that keeps vocal channels open under magical suppression. Immunity to Silence. Resists dark, weak to electric.',
        'min_level': 13, 'rarity': 'rare', 'value': 1500,
        'immunities': ['silence'], 'resistances': ['dark'], 'weaknesses': ['electric'],
        'strength': 0, 'dexterity': 0, 'intelligence': 4, 'constitution': 0,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'ghost_step_anklet',
        'name': 'Ghost Step Anklet',
        'description': 'Weightless metal making footfalls silent. Huge dexterity and crit boost. Resists air and ice, weak to fire.',
        'min_level': 14, 'rarity': 'rare', 'value': 1800,
        'immunities': [], 'resistances': ['air', 'ice'], 'weaknesses': ['fire'],
        'strength': 0, 'dexterity': 8, 'intelligence': 0, 'constitution': 0,
        'crit_bonus': 3.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'spellthread_loop',
        'name': 'Spellthread Loop',
        'description': 'Woven spell-infused thread that concentrates intelligence and amplifies ability potency. Resists light, weak to dark.',
        'min_level': 15, 'rarity': 'rare', 'value': 2000,
        'immunities': [], 'resistances': ['light'], 'weaknesses': ['dark'],
        'strength': 0, 'dexterity': 0, 'intelligence': 8, 'constitution': 0,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': 'amplify_ability',
    },

    # ── LV 16-20 · SUPER RARE ──────────────────────────────────────────────

    {
        'id': 'iron_will_talisman',
        'name': 'Iron Will Talisman',
        'description': 'A dense medallion inscribed with resolve. Immunity to Fear and Confuse. Resists dark and earth, weak to light.',
        'min_level': 16, 'rarity': 'superrare', 'value': 4000,
        'immunities': ['fear', 'confuse'], 'resistances': ['dark', 'earth'], 'weaknesses': ['light'],
        'strength': 4, 'dexterity': 0, 'intelligence': 0, 'constitution': 6,
        'crit_bonus': 0.0, 'damage_bonus': 3, 'special_effect': '',
    },
    {
        'id': 'awakened_eye',
        'name': 'Awakened Eye',
        'description': 'A preserved eye that never sleeps. Immunity to Sleep and Stun. Resists dark, weak to fire.',
        'min_level': 17, 'rarity': 'superrare', 'value': 4500,
        'immunities': ['sleep', 'stun'], 'resistances': ['dark'], 'weaknesses': ['fire'],
        'strength': 0, 'dexterity': 6, 'intelligence': 6, 'constitution': 0,
        'crit_bonus': 2.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'warlord_signet',
        'name': 'Warlord Signet',
        'description': 'A ring worn by a general who never fell. Massive strength and damage. Resists fire and earth, weak to water and ice.',
        'min_level': 18, 'rarity': 'superrare', 'value': 5000,
        'immunities': [], 'resistances': ['fire', 'earth'], 'weaknesses': ['water', 'ice'],
        'strength': 10, 'dexterity': 2, 'intelligence': 0, 'constitution': 6,
        'crit_bonus': 2.0, 'damage_bonus': 8, 'special_effect': '',
    },
    {
        'id': 'ghost_core_pendant',
        'name': 'Ghost Core Pendant',
        'description': 'A hollow crystal containing a compressed spirit. Immunity to Petrify, Stun, and Silence. Resists dark and ice, weak to light.',
        'min_level': 19, 'rarity': 'superrare', 'value': 5500,
        'immunities': ['petrify', 'stun', 'silence'], 'resistances': ['dark', 'ice'], 'weaknesses': ['light'],
        'strength': 0, 'dexterity': 4, 'intelligence': 4, 'constitution': 4,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'apex_hunter_band',
        'name': 'Apex Hunter Band',
        'description': 'Worn by hunters of the unkillable. Sharpens every stat. Resists air and water, weak to dark.',
        'min_level': 20, 'rarity': 'superrare', 'value': 6000,
        'immunities': [], 'resistances': ['air', 'water'], 'weaknesses': ['dark'],
        'strength': 6, 'dexterity': 6, 'intelligence': 4, 'constitution': 4,
        'crit_bonus': 4.0, 'damage_bonus': 5, 'special_effect': '',
    },

    # ── LV 30+ · NOTFOUND ──────────────────────────────────────────────────

    {
        'id': 'voidborn_seal',
        'name': 'Voidborn Seal',
        'description': 'A seal pressed from void-metal. Immunity to all crowd-control. Resists dark, ice, and electric. Weak to light.',
        'min_level': 30, 'rarity': 'notfound', 'value': 14000,
        'immunities': ['petrify', 'stun', 'sleep', 'confuse', 'stun', 'silence'],
        'resistances': ['dark', 'ice', 'electric'], 'weaknesses': ['light'],
        'strength': 8, 'dexterity': 8, 'intelligence': 8, 'constitution': 8,
        'crit_bonus': 3.0, 'damage_bonus': 6, 'special_effect': '',
    },
    {
        'id': 'fracture_core',
        'name': 'Fracture Core',
        'description': 'A crystallised rift shard radiating chaotic energy. Amplifies all outgoing damage. Resists fire and electric, weak to water and ice.',
        'min_level': 30, 'rarity': 'notfound', 'value': 16000,
        'immunities': [], 'resistances': ['fire', 'electric'], 'weaknesses': ['water', 'ice'],
        'strength': 12, 'dexterity': 0, 'intelligence': 12, 'constitution': 0,
        'crit_bonus': 5.0, 'damage_bonus': 14, 'special_effect': 'amplify_ability',
    },
    {
        'id': 'memory_shard',
        'name': 'Memory Shard',
        'description': 'A shard from the Memory Museum. Immunity to Fear and Continuous Damage. Resists dark and light equally — it belongs to neither.',
        'min_level': 35, 'rarity': 'notfound', 'value': 18000,
        'immunities': ['fear', 'continuous_damage'],
        'resistances': ['dark', 'light'], 'weaknesses': [],
        'strength': 0, 'dexterity': 0, 'intelligence': 16, 'constitution': 12,
        'crit_bonus': 0.0, 'damage_bonus': 0, 'special_effect': '',
    },
    {
        'id': 'undying_oath_ring',
        'name': 'Undying Oath Ring',
        'description': 'Forged from the oath of a warrior who refused death. Immunity to all harmful statuses. Resists all elements except light.',
        'min_level': 45, 'rarity': 'notfound', 'value': 28000,
        'immunities': [
            'petrify', 'stun', 'sleep', 'confuse', 'stun', 'silence',
            'fear', 'continuous_damage', 'elemental_debuff',
            'attack_debuff', 'defense_debuff', 'strength_debuff',
            'dexterity_debuff', 'intelligence_debuff', 'constitution_debuff',
        ],
        'resistances': ['dark', 'fire', 'water', 'earth', 'air', 'ice', 'electric'],
        'weaknesses': ['light'],
        'strength': 10, 'dexterity': 10, 'intelligence': 10, 'constitution': 10,
        'crit_bonus': 5.0, 'damage_bonus': 10, 'special_effect': '',
    },
    {
        'id': 'sovereign_emblem',
        'name': 'Sovereign Emblem',
        'description': 'The emblem of an extinct empire. Every stat surges. Immunity to all crowd-control. Resists all elements.',
        'min_level': 60, 'rarity': 'notfound', 'value': 50000,
        'immunities': ['petrify', 'stun', 'sleep', 'confuse', 'stun', 'silence', 'fear'],
        'resistances': ['dark', 'light', 'fire', 'water', 'earth', 'air', 'ice', 'electric'],
        'weaknesses': [],
        'strength': 20, 'dexterity': 20, 'intelligence': 20, 'constitution': 20,
        'crit_bonus': 8.0, 'damage_bonus': 20, 'special_effect': 'amplify_ability',
    },
    {
        'id': 'rotwood_heartstone',
        'name': 'Rotwood Heartstone',
        'description': 'A heartstone from the Rotwood, a forest that has been dead for centuries. Immunity to all harmful statuses. Resists all elements except light.',
        'min_level': 70, 'rarity': 'notfound', 'value': 60000,
        'immunities': [
            'petrify', 'stun', 'sleep', 'confuse', 'stun', 'silence',
            'fear', 'continuous_damage', 'elemental_debuff',
            'attack_debuff', 'defense_debuff', 'strength_debuff',
            'dexterity_debuff', 'intelligence_debuff', 'constitution_debuff',
        ],
        'resistances': ['dark', 'light', 'fire', 'water', 'earth', 'air', 'ice', 'electric'],
        'weaknesses': [],
        'strength': 25, 'dexterity': 25, 'intelligence': 25, 'constitution': 25,
        'crit_bonus': 10.0, 'damage_bonus': 25, 'special_effect': 'auto_revive_1',
    },

    # ── MYTHIC D-CHAIN ACCESSORY REWARDS (notfound) ────────────────────────

    {
        'id': 'mythic_grassland_large_windcarvers_mantle',
        'name': "Windcarver's Mantle",
        'description': 'A mantle woven from windcarve-thread harvested at the peak of a grassland gale rite. Its edges never settle — they move with a wind that is not in the room.',
        'min_level': 1, 'rarity': 'notfound', 'value': 30000,
        'immunities': [], 'resistances': ['air'], 'weaknesses': [],
        'strength': 8, 'dexterity': 24, 'intelligence': 20, 'constitution': 12,
        'crit_bonus': 2.0, 'damage_bonus': 6, 'special_effect': '',
    },
    {
        'id': 'mythic_grassland_small_folklore_hollow_talisman',
        'name': 'Folklore Hollow Talisman',
        'description': 'A talisman carved from hollow-wood found only in the grief-fold — the place where grassland mourning rites end. It carries the weight of names no longer spoken.',
        'min_level': 1, 'rarity': 'notfound', 'value': 22000,
        'immunities': [], 'resistances': ['earth', 'dark'], 'weaknesses': [],
        'strength': 10, 'dexterity': 16, 'intelligence': 18, 'constitution': 14,
        'crit_bonus': 1.5, 'damage_bonus': 4, 'special_effect': '',
    },
    {
        'id': 'mythic_grassland_mid_oathbreakers_sigil',
        'name': "Oathbreaker's Sigil",
        'description': 'A sigil stamp recovered from a sanctum that sealed its own doors — the entity that broke the founding oath left this behind as either warning or trophy.',
        'min_level': 1, 'rarity': 'notfound', 'value': 26000,
        'immunities': ['silence'], 'resistances': ['dark', 'light'], 'weaknesses': [],
        'strength': 14, 'dexterity': 18, 'intelligence': 22, 'constitution': 16,
        'crit_bonus': 2.0, 'damage_bonus': 8, 'special_effect': '',
    },
]

# Export convenience list — mirrors SEED_WEAPON_IDS / SEED_UTILITY_IDS pattern
SEED_ACCESSORY_IDS = [a['id'] for a in ACCESSORY_SEEDS]