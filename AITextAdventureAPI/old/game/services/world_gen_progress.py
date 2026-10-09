"""world_gen_progress: a tiny, pickle-safe progress broadcaster.

World generation (``generate_world``) and intro-story completion are
long-running and were previously only observable via ``print()``. This module
lets those loops *emit* human-readable progress lines to any number of
subscribed listeners (e.g. the in-game loading overlay and the dev TUI "Load
Save" inspector) without the game objects themselves holding references to UI
callbacks -- important because ``PlayerGame`` is pickled when saved, so it must
not carry un-pickleable callables.

Usage (emitter side, e.g. world generation)::

    from game.services import world_gen_progress as progress
    progress.emit(f"[{i}/{n}] Created region '{name}'")

Usage (listener side, e.g. a UI screen)::

    def on_line(line: str) -> None:
        ...  # marshal onto the UI thread

    token = world_gen_progress.subscribe(on_line)
    try:
        ... run the work ...
    finally:
        world_gen_progress.unsubscribe(token)

Listeners are invoked synchronously on the emitting thread, so UI listeners
should marshal onto their own thread (Textual: ``app.call_from_thread``) and
never block. Exceptions raised by a listener are swallowed so one bad listener
can't break generation or sibling listeners.
"""
from __future__ import annotations

import threading
import time
from typing import Callable, Dict

Listener = Callable[[str], None]

_lock = threading.RLock()
_listeners: Dict[int, Listener] = {}
_next_token = 0

# Separate channel for short, PLAYER-FACING status lines (e.g. "Shaping
# continents...", "Connecting the lands (pass 3)..."). The detailed `emit`
# stream above is developer-oriented (timestamps, tile counts, bbox math); the
# loading overlay prefers these friendly lines so the player sees reassuring,
# human-readable progress instead of raw diagnostics.
_status_listeners: Dict[int, Listener] = {}
_next_status_token = 0
_last_status: str | None = None

# Monotonic clock anchor so every emitted line can show elapsed seconds since the
# first emit of a run -- makes bottleneck points obvious in the log stream.
_start_monotonic: float | None = None


def subscribe(listener: Listener) -> int:
    """Register ``listener`` and return a token used to unsubscribe later."""
    global _next_token
    with _lock:
        token = _next_token
        _next_token += 1
        _listeners[token] = listener
    return token


def subscribe_status(listener: Listener) -> int:
    """Register a PLAYER-FACING status listener; returns an unsubscribe token.

    Unlike the previous implementation this does NOT synchronously replay the
    last line to the subscriber: callers (e.g. a Textual screen subscribing from
    the UI/compositor thread) may not legally invoke their thread-marshalling API
    from the subscribing thread. Use :func:`get_last_status` to seed the initial
    value directly on the caller's own thread instead.
    """
    global _next_status_token
    with _lock:
        token = _next_status_token
        _next_status_token += 1
        _status_listeners[token] = listener
    return token


def get_last_status() -> str | None:
    """Return the most recent player-facing status line, or None if none yet.

    Lets a freshly-shown overlay seed its headline from the current status on its
    own thread, avoiding cross-thread replay during subscription.
    """
    with _lock:
        return _last_status



def unsubscribe_status(token: int) -> None:
    """Remove a previously subscribed status listener. Safe to call twice."""
    with _lock:
        _status_listeners.pop(token, None)


def status(line: str) -> None:
    """Broadcast a short, PLAYER-FACING status line (no timestamps/diagnostics).

    Also mirrored into the detailed ``emit`` stream (prefixed) so the dev log
    keeps a record of phase transitions. A failing listener is ignored so it can
    never interrupt generation.
    """
    global _last_status
    text = str(line)
    with _lock:
        _last_status = text
        listeners = list(_status_listeners.values())
    for fn in listeners:
        try:
            fn(text)
        except Exception:  # noqa: BLE001 - never let a UI listener break gen
            pass
    # Keep a breadcrumb in the console/dev log, but do NOT route it through
    # ``emit`` -- that would notify the detailed diagnostic listeners and let a
    # timestamped ``[status]`` line immediately overwrite the friendly headline
    # on any UI that also listens to the diagnostic stream.
    print(f"[status] {text}")



def unsubscribe(token: int) -> None:
    """Remove a previously subscribed listener. Safe to call twice."""
    with _lock:
        _listeners.pop(token, None)


def has_listeners() -> bool:
    with _lock:
        return bool(_listeners)


def emit(line: str) -> None:
    """Broadcast a single progress line to every subscribed listener.

    Each line is prefixed with a wall-clock time and the elapsed seconds since
    the first emit of this run, e.g. ``[14:32:07 +12.4s] ...`` so slow phases
    (bottlenecks) are obvious when scanning the log. Still prints to stdout so
    existing console/log capture keeps working. A failing listener is ignored so
    it can't interrupt generation.
    """
    global _start_monotonic
    now_mono = time.monotonic()
    with _lock:
        if _start_monotonic is None:
            _start_monotonic = now_mono
        elapsed = now_mono - _start_monotonic
    stamp = f"[{time.strftime('%H:%M:%S')} +{elapsed:6.2f}s] "
    text = stamp + str(line)
    print(text)
    with _lock:
        listeners = list(_listeners.values())
    for fn in listeners:
        try:
            fn(text)
        except Exception:  # noqa: BLE001 - never let a UI listener break gen
            pass


def reset_clock() -> None:
    """Reset the elapsed-time anchor so the next emit starts a fresh ``+0.00s``.

    Call at the start of a long-running run (e.g. world generation) so elapsed
    timings are relative to that run rather than the process lifetime.
    """
    global _start_monotonic
    with _lock:
        _start_monotonic = None
        # Also clear the last player-facing status so a new run doesn't replay a
        # stale "done" line to a freshly-subscribed overlay.
        global _last_status
        _last_status = None
