"""
Audio service package for the Fracture TUI.

Provides ``NPCMusicController`` for theme-music playback driven by
NPC ``song_id`` values resolved from ``tui/assets/music``.
"""
from tui.audio.music_controller import NPCMusicController, SongResolution

__all__ = ["NPCMusicController", "SongResolution"]