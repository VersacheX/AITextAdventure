"""
Rule functions that convert a ``ReachabilityResult`` into
``TimelineValidationError`` instances.

Three rule codes (Phase 1):

    TASK_UNCOMPLETABLE_NO_PATH          (error)
        A non-optional task was never completed in any explored state.

    DELIVER_UNCOMPLETABLE_NO_ITEM_PATH  (error)
        A deliver task specifically — names the missing item and cites the
        failure trace.

    REACHABILITY_ANALYSIS_TRUNCATED     (warning)
        BFS was halted before full exploration — results may be incomplete.
        Attached to a synthetic ``_reachability_global`` key, not any task.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Dict, List

from tui.services.dev.dataservices.models import (
    ReachabilityResult,
    TimelineTaskNode,
    TimelineValidationError,
)

_GLOBAL_KEY = "_reachability_global"

# task_id suffixes / types exempt from uncompletable checks (they are
# engine-driven gates, not player-completable objectives)
_EXEMPT_TASK_TYPES = frozenset({
    "complete_intro_story",
    "complete_regional_quests",
    "initialize",
})
_EXEMPT_TASK_SUFFIXES = ("_initialize",)


def _is_exempt(tn: TimelineTaskNode) -> bool:
    task_type = str(tn.task.get("type", "")).lower()
    if task_type in _EXEMPT_TASK_TYPES:
        return True
    for suffix in _EXEMPT_TASK_SUFFIXES:
        if tn.task_id.endswith(suffix):
            return True
    return False


def _err(
    code: str,
    message: str,
    severity: str = "error",
    event_type: str = "",
    related_task_id: str = "",
    related_entity_id: str = "",
) -> TimelineValidationError:
    return TimelineValidationError(
        code=code,
        message=message,
        severity=severity,
        event_type=event_type,
        related_task_id=related_task_id,
        related_entity_id=related_entity_id,
    )


def check_deliver_completability(
    all_tasks: List[TimelineTaskNode],
    result: ReachabilityResult,
) -> Dict[str, List[TimelineValidationError]]:
    """Flag deliver tasks whose required item never reaches them.

    Error code: DELIVER_UNCOMPLETABLE_NO_ITEM_PATH
    """
    errors: Dict[str, List[TimelineValidationError]] = defaultdict(list)

    for tn in all_tasks:
        if _is_exempt(tn):
            continue
        task_type = str(tn.task.get("type", "")).lower()
        if task_type != "deliver":
            continue
        if tn.task_id in result.completable_task_ids:
            continue

        item_id = str(tn.task.get("item_id") or "")
        trace   = result.failure_traces.get(tn.task_id, "No trace available.")
        errors[tn.task_id].append(_err(
            code="DELIVER_UNCOMPLETABLE_NO_ITEM_PATH",
            message=(
                f"Deliver task '{tn.task_id}' requires item '{item_id}' "
                f"but no reachable path provides it. Trace: {trace}"
            ),
            related_entity_id=item_id,
        ))

    return dict(errors)


def check_task_completability(
    all_tasks: List[TimelineTaskNode],
    result: ReachabilityResult,
) -> Dict[str, List[TimelineValidationError]]:
    """Flag non-deliver tasks that were never completed in any explored state.

    Deliver tasks are handled separately by ``check_deliver_completability``
    to give more specific messages.

    Error code: TASK_UNCOMPLETABLE_NO_PATH
    """
    errors: Dict[str, List[TimelineValidationError]] = defaultdict(list)

    for tn in all_tasks:
        if _is_exempt(tn):
            continue
        task_type = str(tn.task.get("type", "")).lower()
        if task_type == "deliver":
            continue  # handled above
        if tn.task_id in result.completable_task_ids:
            continue
        if tn.task_id not in result.reachable_task_ids:
            # R4 (TASK_UNREACHABLE_NO_INBOUND_AWARD) already covers this case
            continue

        trace = result.failure_traces.get(tn.task_id, "No trace available.")
        errors[tn.task_id].append(_err(
            code="TASK_UNCOMPLETABLE_NO_PATH",
            message=(
                f"Task '{tn.task_id}' was activated but never completed "
                f"in any explored state. Trace: {trace}"
            ),
        ))

    return dict(errors)


def check_truncation_warning(
    result: ReachabilityResult,
) -> List[TimelineValidationError]:
    """Return a warning if BFS exploration was truncated.

    Attach to the synthetic ``_reachability_global`` key in the summary dict —
    not to any specific task node.
    """
    if not result.truncated:
        return []

    return [_err(
        code="REACHABILITY_ANALYSIS_TRUNCATED",
        message=(
            f"Reachability analysis explored {result.reachable_states} states "
            f"and was truncated before full coverage. "
            f"TASK_UNCOMPLETABLE_NO_PATH results may be false positives. "
            f"Consider raising max_states or partitioning by chapter."
        ),
        severity="warning",
    )]