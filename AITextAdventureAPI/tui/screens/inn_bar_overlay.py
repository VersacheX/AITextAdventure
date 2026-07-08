"""
InnBarOverlay: floating rest / drink widget for inn and bar shops.

Reuses the ShopOverlay buy flow but is surfaced separately because inn/bar
have no sell mode and their items are plain dicts (not Item objects), so
the detail panel content is different.

This module is a thin re-use shim: it simply constructs and mounts a
ShopOverlay with the correct business_def.  The inn/bar shop-type detection
in ShopOverlay already handles dicts natively, so no extra code is needed.
InnBarOverlay is kept as a named import so OverworldScreen can be explicit
about the intent without hard-coding shop-type strings everywhere.
"""
from __future__ import annotations

from typing import Any, Callable

from tui.screens.shop_overlay import ShopOverlay


def make_inn_bar_overlay(
    pg: Any,
    business_def: dict,
    region: Any,
    on_done: Callable[[bool], None],
) -> ShopOverlay:
    """Return a ShopOverlay configured for an inn or bar business_def."""
    return ShopOverlay(pg, business_def, region, on_done)