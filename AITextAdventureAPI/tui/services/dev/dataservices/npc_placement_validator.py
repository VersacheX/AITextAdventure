"""NPC placement (location) validator.

Validates that ``create_npc`` / ``show_npc`` events place NPCs at a location that
actually exists for the region or city the owning task belongs to.

This is a companion to ``timeline_validator``; the heavier location-grammar
logic lives here and the main validator feeds it the task list plus the loaded
``const`` module.  Call :func:`validate_npc_placements` and merge the returned
``{task_id: [errors]}`` map into the timeline errors.

Location grammar
----------------
A placement ``location`` param is ``(prefix)(token)`` and resolves against the
region or city the task belongs to (derived from the task's ``source_path``,
e.g. ``"regional:desert"``, ``"extended:desert_large"``, ``"main:ch1"``):

    None / "(no location)"      → unplaced. Always safe, never flagged.
    "<...>_center"              → region/city center. Always valid.
    "region_open_area"          → broad wilderness open area (handled by the
    "region_city_open_area"       existing NPC_OPEN_AREA_PLACEMENT warning) —
                                  skipped here.
    "region_<building>"         → a building/area of the owning REGION. The
                                  token must be a region building name.
    "region_city_<building>"    → a building of the owning CITY. The token must
                                  be a city building name (bar, inn, shopitems,
                                  shopweapons, shoparmor, residence*, business*,
                                  hyperway, other1, other2, ...).
    "<region>_<city_type>[...]_<building>"  → cross-city / cross-region placement
                                  (e.g. "desert_mid_city_bar"). The city is
                                  resolved at runtime, but the trailing building
                                  token is static and IS validated against the
                                  union of all known buildings.
    "city_number_<n>[...]_<building>"  → the player's Nth city, resolved at
                                  runtime. As above, the trailing building token
                                  is validated (e.g. the ch5
                                  "city_number_3_region_city_shopitems" pattern).

The runtime placer (``_get_npc_seed_location``) resolves the building with
``location.split('_')[-1]``, so the final segment is always the building name
regardless of the preceding city/region prefix.

Rules
-----
R1  NPC_LOCATION_UNKNOWN_CITY_BUILDING (error)
    ``region_city_<token>`` where ``<token>`` is not a building of the resolved
    city (or, when only the region can be resolved, not a building of ANY city
    of that region).  Also fires for runtime-resolved locations
    (``city_number_<n>_...`` / ``<region>_<city_type>_...``) whose trailing
    building token is not a known building in ANY city or region.

R2  NPC_LOCATION_UNKNOWN_REGION_AREA (error)
    ``region_<token>`` where ``<token>`` is not a building/area of the resolved
    region.

R3  NPC_LOCATION_UNRESOLVED_CONTEXT (warning)
    The owning region/city for the task could not be resolved from its
    ``source_path``, so a ``region_``/``region_city_`` token cannot be checked.
"""
from __future__ import annotations

import logging
import re
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

from tui.services.dev.dataservices.models import (
    TimelineTaskNode,
    TimelineValidationError,
)

log = logging.getLogger(__name__)

# Events that carry a placement ``location`` param.
_PLACEMENT_EVENT_TYPES = frozenset({"create_npc", "show_npc"})

# Region / city taxonomy (mirrors game.constants.REGION_TYPES / CITY_TYPES).
_REGION_TYPES = ("grassland", "desert", "mountains", "shallows", "swamp", "snow", "forest")
_CITY_TYPES = ("large_city", "mid_city", "small_city")

# City-type token as it appears in extended bucket keys ("desert_large").
_CITY_SIZE_TOKENS = ("large", "mid", "small")

# Location tokens that are always valid regardless of region/city buildings.
_ALWAYS_VALID_TOKENS = frozenset({"center", "open_area"})

_CITY_PREFIX = "region_city_"
_REGION_PREFIX = "region_"


# ── const readers ──────────────────────────────────────────────────────────

def _building_names(buildings: Iterable[Any]) -> Set[str]:
    """Return the set of building ``name`` tokens from a BUILDINGS list."""
    out: Set[str] = set()
    for b in buildings or []:
        if isinstance(b, dict) and b.get("name"):
            out.add(str(b["name"]))
    return out


def build_city_building_index(const: Any) -> Tuple[Dict[str, Set[str]], Dict[str, Set[str]]]:
    """Return ``(by_bucket, by_region)`` city-building name sets.

    ``by_bucket``  maps extended bucket keys (e.g. ``"desert_large"``) to the set
                   of valid building name tokens for that specific city.
    ``by_region``  maps a region type (e.g. ``"desert"``) to the union of every
                   building name across its large/mid/small cities.  Used when a
                   task only resolves to a region, not a specific city.

    City buildings are aggregated by ``constants.py`` as
    ``DESERT_LARGE_CITY_BUILDINGS`` etc.
    """
    by_bucket: Dict[str, Set[str]] = {}
    by_region: Dict[str, Set[str]] = {}
    for region in _REGION_TYPES:
        for size in _CITY_SIZE_TOKENS:
            bucket = f"{region}_{size}"
            attr = f"{region.upper()}_{size.upper()}_CITY_BUILDINGS"
            names = _building_names(getattr(const, attr, []) or [])
            if names:
                by_bucket[bucket] = names
                by_region.setdefault(region, set()).update(names)
    return by_bucket, by_region


def build_region_area_index(const: Any) -> Dict[str, Set[str]]:
    """Return ``{region_type: {valid area/building tokens}}``.

    Region buildings are aggregated as ``DESERT_BUILDINGS`` etc.  ``open_area``
    and ``center`` are always valid region tokens.
    """
    index: Dict[str, Set[str]] = {}
    for region in _REGION_TYPES:
        names = _building_names(getattr(const, f"{region.upper()}_BUILDINGS", []) or [])
        names.update(_ALWAYS_VALID_TOKENS)
        index[region] = names
    return index


# ── source_path resolution ─────────────────────────────────────────────────

def _resolve_region_and_city(
    source_path: str,
    chapter_to_city_bucket: Dict[int, str],
) -> Tuple[Optional[str], Optional[str]]:
    """Return ``(region_type, city_bucket)`` for a task ``source_path``.

    ``source_path`` forms:
        "regional:desert"        → region only (no specific city bucket)
        "extended:desert_large"  → region + exact city bucket
        "main:ch1"               → chapter → city bucket → region

    Either element may be ``None`` when it cannot be determined.
    """
    if not source_path or ":" not in source_path:
        return None, None
    group, _, bucket = source_path.partition(":")
    group = group.strip().lower()
    bucket = bucket.strip().lower()

    if group == "extended":
        region = bucket.split("_", 1)[0] if bucket else ""
        return (region if region in _REGION_TYPES else None,
                bucket if bucket else None)

    if group == "regional":
        return (bucket if bucket in _REGION_TYPES else None, None)

    if group == "main":
        m = re.match(r"^ch(\d+)$", bucket)
        if m:
            city_bucket = chapter_to_city_bucket.get(int(m.group(1)))
            if city_bucket:
                region = city_bucket.split("_", 1)[0]
                return (region if region in _REGION_TYPES else None, city_bucket)
    return None, None


# ── location classification ─────────────────────────────────────────────────

def _is_named_city_or_indexed(location: str) -> bool:
    """True for runtime-resolved forms (``<region>_<city_type>`` / ``city_number_``)."""
    if location.startswith("city_number_"):
        return True
    for region in _REGION_TYPES:
        for city_type in _CITY_TYPES:
            if f"{region}_{city_type}" in location:
                return True
    return False


def _building_token(location: str) -> str:
    """Return the trailing building/area token of a location string.

    The runtime placer (``_get_npc_seed_location``) resolves the building/area
    with ``location.split('_')[-1]``, so the final underscore-separated segment
    is always the building name — regardless of whichever city/region prefix
    (``region_``, ``region_city_``, ``city_number_N_...``) precedes it.
    """
    return (location or "").rsplit("_", 1)[-1]


def _err(
    code: str,
    message: str,
    event_type: str,
    npc_id: str,
    severity: str,
) -> TimelineValidationError:
    return TimelineValidationError(
        code=code,
        message=message,
        severity=severity,
        event_type=event_type,
        related_entity_id=npc_id,
    )


def _validate_location(
    location: str,
    event_type: str,
    npc_id: str,
    region_type: Optional[str],
    city_bucket: Optional[str],
    city_by_bucket: Dict[str, Set[str]],
    city_by_region: Dict[str, Set[str]],
    region_areas: Dict[str, Set[str]],
    all_building_tokens: Set[str],
) -> List[TimelineValidationError]:
    """Validate a single resolved location string; return 0..1 errors."""
    loc = (location or "").strip()
    if not loc or loc == "(no location)":
        return []  # unplaced — always safe

    # Broad open-area forms are covered by the timeline validator's
    # NPC_OPEN_AREA_PLACEMENT warning; don't double-report here.
    if loc in ("region_open_area", "region_city_open_area", "city_open_area"):
        return []

    # Runtime-resolved cross-city / indexed placements (``city_number_N_...`` or
    # ``<region>_<city_type>...``).  The *city* is resolved at runtime, but the
    # trailing building token is still static — the placer uses
    # ``location.split('_')[-1]`` to pick the building — so validate that token
    # against the union of every known city/region building.  This keeps the
    # legitimate ch5 ``city_number_3_region_city_shopitems`` pattern silent while
    # still catching a typo'd building name.
    if _is_named_city_or_indexed(loc):
        token = _building_token(loc)
        if token in _ALWAYS_VALID_TOKENS or token in all_building_tokens:
            return []
        return [_err(
            "NPC_LOCATION_UNKNOWN_CITY_BUILDING",
            f"{event_type} for '{npc_id or '?'}' targets building '{token}' "
            f"(via runtime-resolved location '{loc}') which is not a known "
            f"building in any city or region.",
            event_type, npc_id, "error",
        )]

    # ── City building placement ────────────────────────────────────────────
    if loc.startswith(_CITY_PREFIX):
        token = loc[len(_CITY_PREFIX):]
        if token in _ALWAYS_VALID_TOKENS:
            return []
        valid: Optional[Set[str]] = None
        scope = ""
        if city_bucket and city_bucket in city_by_bucket:
            valid = city_by_bucket[city_bucket]
            scope = f"city '{city_bucket}'"
        elif region_type and region_type in city_by_region:
            valid = city_by_region[region_type]
            scope = f"any '{region_type}' city"
        if valid is None:
            return [_err(
                "NPC_LOCATION_UNRESOLVED_CONTEXT",
                f"{event_type} for '{npc_id or '?'}' uses city location '{loc}' "
                f"but the owning city could not be resolved for validation.",
                event_type, npc_id, "warning",
            )]
        if token not in valid:
            return [_err(
                "NPC_LOCATION_UNKNOWN_CITY_BUILDING",
                f"{event_type} for '{npc_id or '?'}' targets building '{token}' "
                f"which does not exist in {scope}.",
                event_type, npc_id, "error",
            )]
        return []

    # ── Region area/building placement ─────────────────────────────────────
    if loc.startswith(_REGION_PREFIX):
        token = loc[len(_REGION_PREFIX):]
        if token in _ALWAYS_VALID_TOKENS:
            return []
        if region_type is None or region_type not in region_areas:
            return [_err(
                "NPC_LOCATION_UNRESOLVED_CONTEXT",
                f"{event_type} for '{npc_id or '?'}' uses region location '{loc}' "
                f"but the owning region could not be resolved for validation.",
                event_type, npc_id, "warning",
            )]
        if token not in region_areas[region_type]:
            return [_err(
                "NPC_LOCATION_UNKNOWN_REGION_AREA",
                f"{event_type} for '{npc_id or '?'}' targets area '{token}' "
                f"which does not exist in region '{region_type}'.",
                event_type, npc_id, "error",
            )]
        return []

    # Anything else is an unrecognized location grammar.
    return [_err(
        "NPC_LOCATION_UNRESOLVED_CONTEXT",
        f"{event_type} for '{npc_id or '?'}' uses unrecognized location "
        f"format '{loc}'.",
        event_type, npc_id, "warning",
    )]


# ── public API ──────────────────────────────────────────────────────────────

def validate_npc_placements(
    tasks: List[TimelineTaskNode],
    const: Any,
    chapter_to_city_bucket: Dict[int, str],
) -> Dict[str, List[TimelineValidationError]]:
    """Validate all NPC placement locations across *tasks*.

    Args:
        tasks:  Flat list of timeline task nodes (each carries ``source_path``
                and the raw ``task`` seed dict).
        const:  The loaded game constants module (source of building lists).
        chapter_to_city_bucket:  ``{chapter_number: city_bucket_key}`` mapping,
                as built by the caller from ``CHAPTER_CITY_ORDER``.

    Returns:
        ``{task_id: [TimelineValidationError, ...]}`` for tasks with findings.
    """
    city_by_bucket, city_by_region = build_city_building_index(const)
    region_areas = build_region_area_index(const)

    # Union of every known city + region building/area token.  Used to validate
    # the trailing building token of runtime-resolved (city_number_N / named
    # city) locations, where the city index is dynamic but the building is not.
    all_building_tokens: Set[str] = set()
    for names in city_by_bucket.values():
        all_building_tokens.update(names)
    for tokens in region_areas.values():
        all_building_tokens.update(tokens)

    results: Dict[str, List[TimelineValidationError]] = {}

    for tn in tasks:
        region_type, city_bucket = _resolve_region_and_city(
            getattr(tn, "source_path", ""), chapter_to_city_bucket
        )
        task = tn.task if isinstance(tn.task, dict) else {}
        stages = (
            (task.get("task_acquire_events") or []),
            (task.get("task_complete_events") or []),
        )
        task_errors: List[TimelineValidationError] = []
        for events in stages:
            for ev in events:
                if not isinstance(ev, dict):
                    continue
                if ev.get("event_type") not in _PLACEMENT_EVENT_TYPES:
                    continue
                params = ev.get("params") or {}
                if not isinstance(params, dict):
                    continue
                location = str(params.get("location") or "")
                npc_id = str(params.get("npc_id") or params.get("id") or "")
                task_errors.extend(_validate_location(
                    location,
                    str(ev.get("event_type")),
                    npc_id,
                    region_type,
                    city_bucket,
                    city_by_bucket,
                    city_by_region,
                    region_areas,
                    all_building_tokens,
                ))
        if task_errors:
            results[tn.task_id] = task_errors

    return results
