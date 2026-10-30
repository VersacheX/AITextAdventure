"""
dev_diagnostics: a developer-only diagnostic channel.

Logic-breaking fall-throughs (an unresolved boss mob, a hostile seed that
can't be generated, a task event that silently no-ops) used to be surfaced by
pushing a "[debug] ..." line into PlayerGame.add_info_dialog_line -- the
*player's* in-game dialog queue. That pollutes the game UI with text the
player should never see.

dev_log instead routes those messages to:

- print (raw stdout, useful for the headless console game / test harness), and
- Python's logging under the "fracture.dev" logger, which the Textual TUI can
  surface in the dev log console (textual console + textual run --dev) via
  self.log / a TextualHandler without corrupting the compositor.

It never writes to the player's info-dialog queue, so diagnostics stay
developer-only.
"""
from __future__ import annotations

import logging

_logger = logging.getLogger("fracture.dev")


def dev_log(message: str, *, source: str | None = None) -> None:
    """Emit a developer-only diagnostic message.

    source is an optional short tag (e.g. "dungeon.get_boss_mob") used to
    prefix the message so logs are traceable. Does NOT surface to the player.
    """
    text = f"[{source}] {message}" if source else message
    try:
        print(f"[dev] {text}")
    except Exception:
        pass
    try:
        _logger.debug(text)
    except Exception:
        pass
    # Mirror into the world-gen progress broadcaster's DEVELOPER-oriented
    # ``emit`` stream. The dev TUI (e.g. Force Complete's ActionReport via
    # ``dev_game_inspector.run_with_report``) captures that broadcaster rather
    # than stdout/logging, so this is what makes diagnostics show up there. The
    # player-facing loading overlay listens on the separate ``status`` channel,
    # so this stays developer-only.
    try:
        from game.services import world_gen_progress as _progress  # noqa: PLC0415
        _progress.emit(text)
    except Exception:
        pass
