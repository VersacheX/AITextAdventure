"""
Tests for tui.audio.music_controller.NPCMusicController.

Covers:
- Song file resolution priority and edge cases
- on_npc_changed with a valid song_id
- on_npc_changed with no song_id (stops current track)
- on_npc_changed with an unresolvable song_id (file missing)
- Same NPC re-selection does not restart the track
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional
from unittest.mock import MagicMock, call, patch

import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

class _FakeRecord:
    """Minimal stand-in for DevRecord with just the fields the controller reads."""
    def __init__(self, id: str, song_id: str = "") -> None:
        self.id      = id
        self.song_id = song_id


def _make_controller(tmp_path: Path, audio_ready: bool = True) -> "NPCMusicController":
    """Build a controller with a mocked-out pygame backend."""
    from tui.audio.music_controller import NPCMusicController

    ctrl = NPCMusicController.__new__(NPCMusicController)
    ctrl._music_dir         = tmp_path
    ctrl._fadeout_ms        = 700
    ctrl._volume            = 0.7
    ctrl._audio_ready       = audio_ready
    ctrl._current_npc_id    = None
    ctrl._current_song_path = None
    return ctrl


# ---------------------------------------------------------------------------
# resolve_song — pure file-system tests (no pygame needed)
# ---------------------------------------------------------------------------

class TestResolveSong:
    def test_prefers_mp3_over_all_others(self, tmp_path: Path) -> None:
        for ext in (".mp3", ".wav", ".ogg", ".m4a", ".mp4"):
            (tmp_path / f"hero{ext}").touch()
        ctrl = _make_controller(tmp_path)
        result = ctrl.resolve_song("hero")
        assert result is not None
        assert result.path.suffix == ".mp3"

    def test_prefers_wav_when_no_mp3(self, tmp_path: Path) -> None:
        (tmp_path / "hero.wav").touch()
        (tmp_path / "hero.ogg").touch()
        ctrl = _make_controller(tmp_path)
        result = ctrl.resolve_song("hero")
        assert result is not None
        assert result.path.suffix == ".wav"

    def test_prefers_ogg_over_m4a_and_mp4(self, tmp_path: Path) -> None:
        (tmp_path / "hero.ogg").touch()
        (tmp_path / "hero.m4a").touch()
        ctrl = _make_controller(tmp_path)
        result = ctrl.resolve_song("hero")
        assert result is not None
        assert result.path.suffix == ".ogg"

    def test_prefers_m4a_over_mp4(self, tmp_path: Path) -> None:
        (tmp_path / "hero.m4a").touch()
        (tmp_path / "hero.mp4").touch()
        ctrl = _make_controller(tmp_path)
        result = ctrl.resolve_song("hero")
        assert result is not None
        assert result.path.suffix == ".m4a"

    def test_returns_none_when_no_match(self, tmp_path: Path) -> None:
        (tmp_path / "other.mp3").touch()
        ctrl = _make_controller(tmp_path)
        assert ctrl.resolve_song("hero") is None

    def test_returns_none_when_dir_missing(self, tmp_path: Path) -> None:
        ctrl = _make_controller(tmp_path / "nonexistent")
        assert ctrl.resolve_song("hero") is None

    def test_case_insensitive_stem_match(self, tmp_path: Path) -> None:
        (tmp_path / "Hero_Instrumental_Skillet.mp3").touch()
        ctrl = _make_controller(tmp_path)
        result = ctrl.resolve_song("hero_instrumental_skillet")
        assert result is not None

    def test_unsupported_extension_ignored(self, tmp_path: Path) -> None:
        (tmp_path / "hero.flac").touch()
        (tmp_path / "hero.aac").touch()
        ctrl = _make_controller(tmp_path)
        assert ctrl.resolve_song("hero") is None

    def test_resolution_carries_correct_song_id(self, tmp_path: Path) -> None:
        (tmp_path / "hero_instrumental_skillet.mp3").touch()
        ctrl = _make_controller(tmp_path)
        result = ctrl.resolve_song("hero_instrumental_skillet")
        assert result is not None
        assert result.song_id == "hero_instrumental_skillet"


# ---------------------------------------------------------------------------
# on_npc_changed — playback behaviour (pygame mocked)
# ---------------------------------------------------------------------------

class TestOnNpcChanged:
    def _ctrl_with_mock_pygame(self, tmp_path: Path) -> tuple:
        """Return (controller, mock_pygame_module)."""
        import tui.audio.music_controller as mod

        mock_pygame = MagicMock()
        mock_pygame.mixer.music.get_busy.return_value = False

        ctrl = _make_controller(tmp_path, audio_ready=True)

        # Patch module-level _pygame used by _play_song / _fadeout_current
        patcher = patch.object(mod, "_pygame", mock_pygame)
        patcher.start()
        return ctrl, mock_pygame, patcher

    def test_plays_track_for_npc_with_valid_song(self, tmp_path: Path) -> None:
        (tmp_path / "hero_instrumental_skillet.mp3").touch()
        ctrl, mock_pg, patcher = self._ctrl_with_mock_pygame(tmp_path)
        try:
            ctrl.on_npc_changed(_FakeRecord("chock", "hero_instrumental_skillet"))
            mock_pg.mixer.music.load.assert_called_once()
            mock_pg.mixer.music.play.assert_called_once()
        finally:
            patcher.stop()

    def test_no_play_when_song_id_missing(self, tmp_path: Path) -> None:
        ctrl, mock_pg, patcher = self._ctrl_with_mock_pygame(tmp_path)
        try:
            ctrl.on_npc_changed(_FakeRecord("chock", ""))
            mock_pg.mixer.music.load.assert_not_called()
            mock_pg.mixer.music.play.assert_not_called()
        finally:
            patcher.stop()

    def test_no_play_when_file_not_found(self, tmp_path: Path) -> None:
        ctrl, mock_pg, patcher = self._ctrl_with_mock_pygame(tmp_path)
        try:
            ctrl.on_npc_changed(_FakeRecord("chock", "missing_track"))
            mock_pg.mixer.music.load.assert_not_called()
            mock_pg.mixer.music.play.assert_not_called()
        finally:
            patcher.stop()

    def test_fadeout_on_npc_change_even_without_new_track(self, tmp_path: Path) -> None:
        ctrl, mock_pg, patcher = self._ctrl_with_mock_pygame(tmp_path)
        mock_pg.mixer.music.get_busy.return_value = True
        # Simulate a currently playing track
        ctrl._current_npc_id = "old_npc"
        try:
            ctrl.on_npc_changed(_FakeRecord("chock", ""))
            mock_pg.mixer.music.fadeout.assert_called_once_with(700)
        finally:
            patcher.stop()

    def test_same_npc_reselection_does_not_restart(self, tmp_path: Path) -> None:
        (tmp_path / "hero_instrumental_skillet.mp3").touch()
        ctrl, mock_pg, patcher = self._ctrl_with_mock_pygame(tmp_path)
        try:
            ctrl.on_npc_changed(_FakeRecord("chock", "hero_instrumental_skillet"))
            # Reset call counts, then re-select the same NPC
            mock_pg.mixer.music.load.reset_mock()
            mock_pg.mixer.music.play.reset_mock()
            ctrl.on_npc_changed(_FakeRecord("chock", "hero_instrumental_skillet"))
            mock_pg.mixer.music.load.assert_not_called()
            mock_pg.mixer.music.play.assert_not_called()
        finally:
            patcher.stop()

    def test_npc_with_no_id_is_ignored(self, tmp_path: Path) -> None:
        ctrl, mock_pg, patcher = self._ctrl_with_mock_pygame(tmp_path)
        try:
            ctrl.on_npc_changed(object())  # no id / npc_id attribute
            mock_pg.mixer.music.load.assert_not_called()
        finally:
            patcher.stop()

    def test_audio_not_ready_does_not_crash(self, tmp_path: Path) -> None:
        (tmp_path / "hero_instrumental_skillet.mp3").touch()
        ctrl = _make_controller(tmp_path, audio_ready=False)
        # Should silently no-op without raising
        ctrl.on_npc_changed(_FakeRecord("chock", "hero_instrumental_skillet"))

    def test_shutdown_calls_fadeout(self, tmp_path: Path) -> None:
        ctrl, mock_pg, patcher = self._ctrl_with_mock_pygame(tmp_path)
        mock_pg.mixer.music.get_busy.return_value = True
        try:
            ctrl.shutdown()
            mock_pg.mixer.music.fadeout.assert_called_once_with(700)
        finally:
            patcher.stop()