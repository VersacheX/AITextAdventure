"""
Special-item integrity validator.

Rules
-----
E1  SPECIAL_ITEM_NO_SOURCE  (error)
    The item has no award_item or dungeon_add_treasure event anywhere in the
    loaded timeline.  It is unreachable by the player through normal play.

E2  SPECIAL_ITEM_IMPOSSIBLE_COUNTS  (error)
    The total number of remove_item events for this item across the entire
    timeline exceeds the total number of award_item + dungeon_add_treasure
    events.  The game can never give the player enough copies to satisfy all
    removals.

I1  SPECIAL_ITEM_NEVER_REMOVED  (info)
    The item is given (at least one award_item or dungeon_add_treasure) but
    is never removed by any remove_item event.  This is not necessarily wrong
    but may indicate an incomplete quest flow.
"""
from __future__ import annotations

from typing import Any, Dict, List

from tui.services.dev.dataservices.models import SpecialItemValidationError


def _err(code: str, message: str, severity: str = "error") -> SpecialItemValidationError:
    return SpecialItemValidationError(code=code, message=message, severity=severity)


def _build_source_counts(groups: list) -> Dict[str, Dict[str, int]]:
    """Walk every task event and count award, dungeon, and remove occurrences
    per item_id.

    Returns {item_id: {"award": n, "dungeon": n, "remove": n}}.
    """
    counts: Dict[str, Dict[str, int]] = {}

    for group in groups:
        for bucket in group.buckets:
            for tn in bucket.tasks:
                task = tn.task
                for stage in ("task_acquire_events", "task_complete_events"):
                    for ev in (task.get(stage) or []):
                        if not isinstance(ev, dict):
                            continue
                        et     = ev.get("event_type", "")
                        params = ev.get("params") or {}
                        iid    = str(
                            params.get("item_id") or params.get("id") or ""
                        ).strip()
                        if not iid:
                            continue

                        if et == "award_item":
                            c = counts.setdefault(iid, {"award": 0, "dungeon": 0, "remove": 0})
                            c["award"] += 1
                        elif et == "dungeon_add_treasure":
                            c = counts.setdefault(iid, {"award": 0, "dungeon": 0, "remove": 0})
                            c["dungeon"] += 1
                        elif et == "remove_item":
                            c = counts.setdefault(iid, {"award": 0, "dungeon": 0, "remove": 0})
                            c["remove"] += 1

    return counts


def validate_special_items(records: list, timeline_groups: list) -> Dict[str, Any]:
    """Validate all special-item DevRecords against the full timeline tree.

    Annotates each record's ``extras["_errors"]`` with a list of
    ``SpecialItemValidationError`` objects and sets ``extras["_validated"] = True``.

    Returns a summary dict with ``total_errors``, ``invalid``, and
    ``by_code`` tallies.
    """
    source_counts = _build_source_counts(timeline_groups)

    by_code: Dict[str, int] = {}
    total_errors = 0
    invalid      = 0

    for record in records:
        record.extras["_errors"]    = []
        record.extras["_validated"] = True

        c      = source_counts.get(record.id, {"award": 0, "dungeon": 0, "remove": 0})
        give   = c["award"] + c["dungeon"]
        remove = c["remove"]

        if give == 0:
            # E1 — unreachable
            err = _err(
                "SPECIAL_ITEM_NO_SOURCE",
                f"'{record.id}' has no award_item or dungeon_add_treasure event in the "
                f"timeline.  The item is unreachable through normal play.",
            )
            record.extras["_errors"].append(err)
            by_code["SPECIAL_ITEM_NO_SOURCE"] = by_code.get("SPECIAL_ITEM_NO_SOURCE", 0) + 1
            total_errors += 1
            invalid      += 1
        else:
            if remove > give:
                # E2 — impossible give/remove ratio
                err = _err(
                    "SPECIAL_ITEM_IMPOSSIBLE_COUNTS",
                    f"'{record.id}' is given {give} time(s) but removed {remove} time(s).  "
                    f"There are more removals than possible awards, which is impossible to satisfy.",
                )
                record.extras["_errors"].append(err)
                by_code["SPECIAL_ITEM_IMPOSSIBLE_COUNTS"] = (
                    by_code.get("SPECIAL_ITEM_IMPOSSIBLE_COUNTS", 0) + 1
                )
                total_errors += 1
                invalid      += 1

            if remove == 0:
                # I1 — given but never removed
                info = _err(
                    "SPECIAL_ITEM_NEVER_REMOVED",
                    f"'{record.id}' is given {give} time(s) but is never removed by any "
                    f"remove_item event.  Verify this is intentional.",
                    severity="info",
                )
                record.extras["_errors"].append(info)
                by_code["SPECIAL_ITEM_NEVER_REMOVED"] = (
                    by_code.get("SPECIAL_ITEM_NEVER_REMOVED", 0) + 1
                )
                total_errors += 1

    return {
        "total_errors": total_errors,
        "invalid":      invalid,
        "by_code":      by_code,
    }
