"""
NPCMusicController — theme-music playback for TUI NPC selection.

Resolves ``<song_id>.*`` from a music directory and plays/fades tracks via
``pygame.mixer.music``.  All audio failures are caught and logged so the TUI
never crashes due to audio issues.

Playback rules
--------------
- NPC changes → fade out current track, start new track if one is resolved.
- NPC has no ``song_id`` or no matching file → fade out only; no new track.
- Same NPC re-selected → no-op (track is not restarted).
- ``shutdown()`` → fade out and release resources; call on screen unmount.

Extension priority (highest → lowest): .mp3, .wav, .ogg, .m4a, .mp4
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Optional pygame import — degrades gracefully if not installed / no audio
# ---------------------------------------------------------------------------
try:
    import pygame as _pygame  # type: ignore[import-untyped]
    _PYGAME_AVAILABLE = True
except ImportError:
    _pygame = None  # type: ignore[assignment]
    _PYGAME_AVAILABLE = False
    logger.warning("NPC music disabled: pygame is not installed.")


@dataclass(frozen=True)
class SongResolution:
    """A successfully resolved audio file for a given song_id."""

    song_id: str
    path: Path


class NPCMusicController:
    """Handles NPC theme-music playback for a single TUI screen lifetime.

    Parameters
    ----------
    music_dir:
        Directory to search for ``<song_id>.*`` audio files.
    fadeout_ms:
        Duration in milliseconds for the fade-out transition between tracks.
    volume:
        Playback volume in the range ``[0.0, 1.0]``.
    """

    _SUPPORTED_EXTS_IN_PRIORITY: tuple[str, ...] = (
        ".mp3", ".wav", ".ogg", ".m4a", ".mp4"
    )

    def __init__(
        self,
        music_dir: Path,
        fadeout_ms: int = 700,
        volume: float = 0.7,
    ) -> None:
        self._music_dir   = music_dir
        self._fadeout_ms  = fadeout_ms
        self._volume      = max(0.0, min(volume, 1.0))
        self._audio_ready = False

        self._current_npc_id:   Optional[str]  = None
        self._current_song_path: Optional[Path] = None

        self._ensure_audio_initialized()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def on_npc_changed(self, npc: object) -> None:
        """Respond to an NPC selection change.

        ``npc`` must expose an ``id`` (or ``npc_id``) attribute and a
        ``song_id`` attribute — a ``DevRecord`` satisfies both.

        Behaviour:
        - Same NPC as current → no-op.
        - New NPC with resolvable track → fade out current, play new.
        - New NPC without track → fade out current, do not start new.
        """
        npc_id  = self._read_attr(npc, "id") or self._read_attr(npc, "npc_id")
        song_id = self._read_attr(npc, "song_id")

        if npc_id is None:
            logger.warning("NPC music: incoming npc has no id attribute; ignoring.")
            return

        npc_id_str = str(npc_id)

        # Same NPC re-selected — do not restart the track.
        if npc_id_str == self._current_npc_id:
            return

        self._current_npc_id = npc_id_str
        self._fadeout_current()

        if not song_id:
            self._current_song_path = None
            return

        resolution = self.resolve_song(str(song_id))
        if resolution is None:
            logger.info("NPC music: no audio file found for song_id=%r", song_id)
            self._current_song_path = None
            return

        self._play_song(resolution.path)

    def resolve_song(self, song_id: str) -> Optional[SongResolution]:
        """Resolve *song_id* to a ``Path`` under ``music_dir``.

        Scans ``music_dir`` for a file whose stem matches ``song_id``
        (case-insensitive) and whose extension is in the supported set.
        When multiple matches exist they are sorted by extension priority
        then lexicographically by filename — the first result is returned.

        Returns ``None`` if the directory is missing, empty, or no match
        is found.
        """
        if not self._music_dir.exists() or not self._music_dir.is_dir():
            logger.warning("NPC music: directory missing or not a dir: %s", self._music_dir)
            return None

        target_stem = song_id.lower()
        supported   = set(self._SUPPORTED_EXTS_IN_PRIORITY)
        candidates: list[Path] = []

        for p in self._music_dir.iterdir():
            if not p.is_file():
                continue
            if p.stem.lower() != target_stem:
                continue
            if p.suffix.lower() not in supported:
                continue
            candidates.append(p)

        if not candidates:
            return None

        ext_rank = {ext: i for i, ext in enumerate(self._SUPPORTED_EXTS_IN_PRIORITY)}
        candidates.sort(key=lambda p: (ext_rank.get(p.suffix.lower(), 999), p.name.lower()))
        return SongResolution(song_id=song_id, path=candidates[0])

    def stop(self) -> None:
        """Fade out the currently playing track and clear the song pointer."""
        self._fadeout_current()
        self._current_song_path = None

    def shutdown(self) -> None:
        """Stop playback and release resources.  Call on screen unmount."""
        self.stop()
        # Do not call pygame.quit() — the application may still be running
        # other screens that rely on pygame internals.

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _ensure_audio_initialized(self) -> None:
        """Attempt to initialise the pygame mixer; set ``_audio_ready``."""
        if not _PYGAME_AVAILABLE:
            return
        try:
            if not _pygame.get_init():
                _pygame.init()
            if not _pygame.mixer.get_init():
                _pygame.mixer.init()
            _pygame.mixer.music.set_volume(self._volume)
            self._audio_ready = True
        except Exception as exc:
            self._audio_ready = False
            logger.warning("NPC music: pygame mixer init failed — audio disabled: %s", exc)

    def _play_song(self, path: Path) -> None:
        """Load and loop a track from *path* with a short fade-in."""
        if not self._audio_ready:
            return
        try:
            _pygame.mixer.music.load(str(path))
            _pygame.mixer.music.play(loops=-1, fade_ms=200)
            self._current_song_path = path
            logger.info("NPC music: playing %s", path.name)
        except Exception as exc:
            self._current_song_path = None
            logger.warning("NPC music: failed to play %s — %s", path, exc)

    def _fadeout_current(self) -> None:
        """Fade out the currently playing track, if any."""
        if not self._audio_ready:
            return
        try:
            if _pygame.mixer.music.get_busy():
                _pygame.mixer.music.fadeout(self._fadeout_ms)
        except Exception as exc:
            logger.warning("NPC music: fadeout failed — %s", exc)

    @staticmethod
    def _read_attr(obj: object, attr: str) -> Optional[object]:
        """Safely read *attr* from *obj*, returning ``None`` on any error."""
        try:
            return getattr(obj, attr, None)
        except Exception:
            return None