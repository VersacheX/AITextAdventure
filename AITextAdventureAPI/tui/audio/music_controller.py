"""
NPCMusicController — theme-music playback for TUI NPC selection.

Resolves ``<song_id>.*`` from a music directory and plays/fades tracks via
``pygame.mixer.music``.  All audio failures are caught and logged so the TUI
never crashes due to audio issues.

Playback rules
--------------
- NPC changes → fade out current track, start new track if one is resolved.
- NPC has no ``song_id`` or no matching file → fade out only; no new track.
- Same NPC re-selected → no-op unless ``force=True``.
- Tracks always play once (``loops=0``); poll ``poll_song_ended()`` to detect
  end and advance or replay depending on autoplay state.
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
    # Reserve a USEREVENT slot for music-end detection.
    # Set before any mixer call so it's stable at module load time.
    _MUSIC_ENDEVENT: int = _pygame.USEREVENT + 1
except ImportError:
    _pygame = None  # type: ignore[assignment]
    _PYGAME_AVAILABLE = False
    _MUSIC_ENDEVENT: int = 0
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
        self._paused      = False

        self._current_npc_id:    Optional[str]  = None
        self._current_song_path: Optional[Path] = None

        self._ensure_audio_initialized()

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def current_npc_id(self) -> Optional[str]:
        """The npc_id of the currently loaded track, or ``None``."""
        return self._current_npc_id

    @property
    def current_song_name(self) -> str:
        """Filename stem of the currently loaded track, or empty string."""
        return self._current_song_path.stem if self._current_song_path else ""

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def on_npc_changed(self, npc: object) -> None:
        """Respond to an NPC selection change driven by tree selection.

        ``npc`` must expose ``id`` (or ``npc_id``) and ``song_id`` — a
        ``DevRecord`` satisfies both.

        Same NPC re-selected → no-op (music does not restart).
        """
        npc_id  = self._read_attr(npc, "id") or self._read_attr(npc, "npc_id")
        song_id = self._read_attr(npc, "song_id")

        if npc_id is None:
            logger.warning("NPC music: incoming npc has no id attribute; ignoring.")
            return

        self.play_record(str(npc_id), str(song_id) if song_id else "", force=False)

    def play_record(self, npc_id: str, song_id: str, *, force: bool = False) -> bool:
        """Play the track for *npc_id*/*song_id*.

        Parameters
        ----------
        npc_id:
            Identifier used for same-NPC deduplication.
        song_id:
            Key to resolve the audio file from ``music_dir``.
        force:
            When ``True`` bypasses the same-NPC guard — used by the player
            widget for prev/next/autoplay advances.

        Returns ``True`` if playback was (re-)started.
        """
        if not force and npc_id == self._current_npc_id:
            return False

        self._current_npc_id = npc_id
        self._paused = False
        self._fadeout_current()

        if not song_id:
            self._current_song_path = None
            return False

        resolution = self.resolve_song(song_id)
        if resolution is None:
            logger.info("NPC music: no audio file found for song_id=%r", song_id)
            self._current_song_path = None
            return False

        self._play_song(resolution.path)
        return True

    def toggle_pause(self) -> bool:
        """Pause if playing; unpause if paused.  Returns new paused state."""
        if not self._audio_ready:
            return self._paused
        try:
            if self._paused:
                _pygame.mixer.music.unpause()
                self._paused = False
            else:
                _pygame.mixer.music.pause()
                self._paused = True
        except Exception as exc:
            logger.warning("NPC music: pause toggle failed — %s", exc)
        return self._paused

    @property
    def is_paused(self) -> bool:
        return self._paused

    def is_playing(self) -> bool:
        """True if a track is loaded and not paused."""
        if not self._audio_ready:
            return False
        try:
            return bool(_pygame.mixer.music.get_busy()) and not self._paused
        except Exception:
            return False

    def poll_song_ended(self) -> bool:
        """Consume and return ``True`` if the current track just ended naturally.

        Call from a polling timer.  Returns at most once per real song end —
        stale end-events left over from fadeouts triggered by prev/next skips
        are discarded by checking whether music is already playing again.
        """
        if not self._audio_ready or self._paused:
            return False
        try:
            events = _pygame.event.get(_MUSIC_ENDEVENT)
            if not events:
                return False
            # Guard: if a new track is already playing, the event is stale
            # (produced by a fadeout from a skip, not a natural song end).
            if _pygame.mixer.music.get_busy():
                return False
            return True
        except Exception:
            return False

    def resolve_song(self, song_id: str) -> Optional[SongResolution]:
        """Resolve *song_id* to a ``Path`` under ``music_dir``.

        Scans ``music_dir`` for a file whose stem matches ``song_id``
        (case-insensitive) with a supported extension. When multiple matches
        exist, sorted by extension priority then lexicographically.

        Returns ``None`` if directory is missing, empty, or no match found.
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
        self._paused = False

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
            # Register end-of-track event so poll_song_ended() works.
            _pygame.mixer.music.set_endevent(_MUSIC_ENDEVENT)
            self._audio_ready = True
        except Exception as exc:
            self._audio_ready = False
            logger.warning("NPC music: pygame mixer init failed — audio disabled: %s", exc)

    def _play_song(self, path: Path) -> None:
        """Load and play *path* once (``loops=0``).

        Plays once so ``poll_song_ended()`` fires at track end, enabling
        autoplay advancement or replay depending on the player widget state.

        After starting playback any stale ``_MUSIC_ENDEVENT`` events queued
        by a previous ``fadeout()`` call are cleared so rapid prev/next
        navigation cannot produce spurious poll triggers.
        """
        if not self._audio_ready:
            return
        try:
            _pygame.mixer.music.load(str(path))
            _pygame.mixer.music.play(loops=0, fade_ms=200)
            self._current_song_path = path
            self._paused = False
            # Discard any end-events left over from the previous fadeout.
            # fadeout() is asynchronous — it posts _MUSIC_ENDEVENT when the
            # fade completes, which can be *after* the new track has started.
            # Clearing here prevents those stale events from tricking
            # poll_song_ended() into firing an unwanted advance.
            _pygame.event.clear(_MUSIC_ENDEVENT)
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
    def _read_attr(obj: object, attr: str) -> Optional[str]:
        """Safely read a string attribute from *obj*."""
        val = getattr(obj, attr, None)
        return str(val) if val is not None else None