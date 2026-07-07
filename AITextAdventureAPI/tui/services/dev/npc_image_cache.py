"""Module-level two-level ANSI portrait cache.

Level 1 — in-process memory dict (instant, per-run).
Level 2 — disk sidecar ``*.ansi`` stored beside the source image asset
          (survives process restarts; invalidated when source is newer).

Key format: (str(image_path), cols, rows, renderer)
renderer is always "chafa" or "braille"
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

# ── module-level memory cache ────────────────────────────────────────────────
# Key: (str(image_path), cols, rows, renderer)  renderer ∈ {"chafa", "braille"}
_MEMORY_CACHE: dict[tuple[str, int, int, str], str] = {}


def _sidecar_path(image_path: Path, cols: int, rows: int, renderer: str) -> Path:
    """Return the sidecar ``.ansi`` path for this (image, size, renderer) combo."""
    return image_path.parent / f"{image_path.stem}_{cols}x{rows}_{renderer}.ansi"


def get_cached(
    image_path: Path, cols: int, rows: int, renderer: str
) -> Optional[str]:
    """Return cached ANSI text, or ``None`` on a cache miss.

    Lookup order:
        1. In-process memory cache (instant hit).
        2. Disk sidecar — invalidated if the source image is newer.

    All ``OSError`` are swallowed; returns ``None`` on any I/O failure.
    """
    key: tuple[str, int, int, str] = (str(image_path), cols, rows, renderer)

    # Level 1: memory
    hit = _MEMORY_CACHE.get(key)
    if hit is not None:
        return hit

    # Level 2: disk sidecar
    try:
        sidecar = _sidecar_path(image_path, cols, rows, renderer)
        if not sidecar.exists():
            return None
        # Source image newer than sidecar → stale, re-render
        if image_path.stat().st_mtime > sidecar.stat().st_mtime:
            return None
        ansi = sidecar.read_text(encoding="utf-8")
        _MEMORY_CACHE[key] = ansi
        return ansi
    except OSError:
        return None


def store(
    image_path: Path, cols: int, rows: int, renderer: str, ansi: str
) -> None:
    """Persist *ansi* in both the memory cache and the disk sidecar.

    Disk write is best-effort — a read-only filesystem must never crash the app.
    """
    key: tuple[str, int, int, str] = (str(image_path), cols, rows, renderer)
    _MEMORY_CACHE[key] = ansi

    try:
        sidecar = _sidecar_path(image_path, cols, rows, renderer)
        sidecar.write_text(ansi, encoding="utf-8")
    except OSError:
        pass


def invalidate(image_path: Path) -> None:
    """Evict all in-memory cache entries for *image_path*.

    Does **not** touch disk sidecars.
    """
    target = str(image_path)
    for key in list(_MEMORY_CACHE.keys()):
        if key[0] == target:
            del _MEMORY_CACHE[key]


def clear_disk_sidecars(image_path: Path) -> int:
    """Delete all ``*.ansi`` sidecars beside *image_path*.  Returns count deleted."""
    count = 0
    pattern = f"{image_path.stem}_*x*_*.ansi"
    for sidecar in image_path.parent.glob(pattern):
        try:
            sidecar.unlink()
            count += 1
        except OSError:
            pass
    return count