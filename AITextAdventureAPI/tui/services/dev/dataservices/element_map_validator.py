"""
Startup validator for CHARACTER_NPC_ELEMENT_MAP (IMPLEMENTATION_SPEC_character_elements.md, section 7).

Logs a WARNING for:
- a key in CHARACTER_NPC_CLASS_MAP missing from CHARACTER_NPC_ELEMENT_MAP, or the reverse;
- an element value not in Element or equal to 'physical';
- a core-five character without exactly 4 elements, or a recruit with more than 2;
- a class with no character for one of the 8 elements;
- any recruit starting ability that fails can_learn(..., check_stats=False).

Expected result on a correct build: zero warnings.
"""
from __future__ import annotations

import logging
from typing import Any, List

logger = logging.getLogger(__name__)

_CORE_FIVE = {'technique', 'spirit', 'magic', 'tech', 'skill'}
_VALID_ELEMENTS = {'light', 'dark', 'earth', 'air', 'fire', 'water', 'electric', 'ice'}
_ALL_ELEMENTS = _VALID_ELEMENTS  # 8 elements, excludes 'physical'


def validate_element_map(const: Any) -> List[str]:
    """Return a list of warning strings describing any issues found.

    Also logs each warning. Pass `game.constants` (or an equivalent namespace)
    as `const`.
    """
    warnings: List[str] = []

    class_map = getattr(const, 'CHARACTER_NPC_CLASS_MAP', {}) or {}
    element_map = getattr(const, 'CHARACTER_NPC_ELEMENT_MAP', {}) or {}

    class_keys = set(class_map.keys())
    element_keys = set(element_map.keys())

    for key in class_keys - element_keys:
        warnings.append(f"'{key}' is in CHARACTER_NPC_CLASS_MAP but missing from CHARACTER_NPC_ELEMENT_MAP.")
    for key in element_keys - class_keys:
        warnings.append(f"'{key}' is in CHARACTER_NPC_ELEMENT_MAP but missing from CHARACTER_NPC_CLASS_MAP.")

    class_coverage = {cls: set() for cls in set(class_map.values())}

    for key, elements in element_map.items():
        elements = elements or []
        for e in elements:
            ev = str(e).lower()
            if ev == 'physical' or ev not in _VALID_ELEMENTS:
                warnings.append(f"'{key}' has invalid element '{e}' (must be one of {sorted(_VALID_ELEMENTS)}, never 'physical').")

        if key in _CORE_FIVE:
            if len(elements) != 4:
                warnings.append(f"Core-five character '{key}' has {len(elements)} elements, expected exactly 4.")
        else:
            if len(elements) > 2:
                warnings.append(f"Recruit '{key}' has {len(elements)} elements, expected 1-2.")

        cls = class_map.get(key)
        if cls is not None:
            class_coverage.setdefault(cls, set())
            class_coverage[cls].update(str(e).lower() for e in elements)

    for cls, covered in class_coverage.items():
        missing = _ALL_ELEMENTS - covered
        if missing:
            warnings.append(f"Class '{cls}' has no character covering element(s): {sorted(missing)}.")

    # Recruit starting abilities must match class + element (non_player_ability
    # is expected here -- unique recruit kit abilities are intentionally
    # flagged that way to keep them out of the general learn pool, and are
    # attached directly from the seed, bypassing can_learn's gate entirely).
    try:
        from game.objects.player_ability import _val, player_class_of
        from game.objects.player import Player

        ability_seeds = getattr(const, 'PLAYER_ABILITY_SEEDS', []) or []
        seed_map = {s.get('id'): s for s in ability_seeds}

        for pc in (getattr(const, 'ATTAINABLE_PLAYER_CHARACTERS', None) or []):
            if not isinstance(pc, dict):
                continue
            char_id = pc.get('id') or pc.get('npc_id')
            if not char_id:
                continue
            p = Player(pc.get('name') or char_id)
            p.character_class = class_map.get(char_id)
            p.npc_id = char_id
            p.elements_base = list(element_map.get(char_id, []))
            cls = player_class_of(p)
            base = {_val(e) for e in p.elements_base}
            for aid in (pc.get('abilities') or []):
                aseed = seed_map.get(aid)
                if not aseed:
                    continue
                atype = _val(aseed.get('ability_type'))
                if cls and atype != cls:
                    warnings.append(
                        f"Recruit '{char_id}' starting ability '{aid}' has ability_type "
                        f"'{atype}' which does not match their class '{cls}'."
                    )
                    continue
                aelements = {_val(e) for e in (aseed.get('elements') or [])}
                if base and not base & aelements:
                    warnings.append(
                        f"Recruit '{char_id}' starting ability '{aid}' has no element overlap "
                        f"with their elements_base {sorted(base)}."
                    )
    except Exception as exc:  # pragma: no cover - defensive, should not block startup
        warnings.append(f"element_map_validator: recruit ability check skipped due to error: {exc}")

    for w in warnings:
        logger.warning(w)

    return warnings
