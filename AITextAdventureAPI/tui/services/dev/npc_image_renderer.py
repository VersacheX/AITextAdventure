"""
npc_image_renderer: converts a PIL Image to a braille + truecolor ANSI string
suitable for display in a Textual Static widget (via Rich Text.from_ansi()).

Encoding
────────
Each terminal character cell encodes a 2×4 pixel block using a Unicode braille
codepoint (U+2800–U+28FF).  Each cell carries BOTH a foreground colour (average
RGB of lit dots) and a background colour (average RGB of unlit dots), so every
pixel contributes visible colour — identical in principle to the half-block
technique but at 2×4 resolution instead of 1×2.

Threshold is computed **per cell** from the local median of the 8 pixels in
that cell.  This means sky cells and face cells each split ~4 lit / 4 dark
independently — a bright region can never steal dots from a dark region or
vice versa.  The result preserves local detail everywhere regardless of global
brightness variation.

Braille dot layout (2 cols × 4 rows per cell):

    col 0  col 1
row 0:  dot0   dot3
row 1:  dot1   dot4
row 2:  dot2   dot5
row 3:  dot6   dot7

Bit mapping (Unicode braille standard):
    dot0=0x01  dot1=0x02  dot2=0x04  dot3=0x08
    dot4=0x10  dot5=0x20  dot6=0x40  dot7=0x80
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

_DOT_BITS = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

# (row_within_4, col_within_2) for each of the 8 braille dots
_DOT_POS = [
    (0, 0), (1, 0), (2, 0),   # dots 0-2: left column rows 0-2
    (0, 1), (1, 1), (2, 1),   # dots 3-5: right column rows 0-2
    (3, 0), (3, 1),            # dots 6-7: bottom row
]


def _luminance(r: int, g: int, b: int) -> float:
    return 0.299 * r + 0.587 * g + 0.114 * b


def image_to_braille_ansi(
    image: "PIL.Image.Image",  # type: ignore[name-defined]
    cols: int = 60,
    rows: int = 28,
    threshold: Optional[float] = None,
) -> str:
    """Convert *image* to a braille + truecolor ANSI string.

    Each braille cell carries both a foreground colour (average RGB of lit
    dots) and a background colour (average RGB of unlit dots).  The dot
    threshold is computed **per cell** from the local median luminance of the
    8 pixels in that cell, so every region of the image — bright sky, dark
    shadows, mid-tone skin — independently splits its dots ~50/50.  A global
    bright region can never dominate the dot budget of a darker region.

    Args:
        image:     A PIL Image (any mode; converted to RGB internally).
        cols:      Target character columns.  Each col = 2 source pixels wide.
        rows:      Target character rows.     Each row = 4 source pixels tall.
        threshold: If given, override per-cell adaptive threshold with a fixed
                   global luminance value (0–255).  Useful for debugging only.

    Returns:
        A plain string with ANSI SGR truecolor codes and braille codepoints.
        Pass to ``Rich.Text.from_ansi()`` before handing to a Textual Static.
    """
    try:
        from PIL import Image as PilImage  # noqa: PLC0415
    except ImportError:
        return "(Pillow not installed — cannot render image)"

    # ── resize to exact braille pixel grid ────────────────────────────────
    px_w = cols * 2
    px_h = rows * 4
    img = image.convert("RGB").resize((px_w, px_h), PilImage.LANCZOS)
    pixels = img.load()

    # ── render ─────────────────────────────────────────────────────────────
    RESET = "\033[0m"
    lines: list[str] = []

    for cell_row in range(rows):
        row_chars: list[str] = []
        py_base = cell_row * 4

        for cell_col in range(cols):
            px_base = cell_col * 2

            # Collect all 8 pixel colours for this cell up front
            cell_pixels: list[tuple[int, int, int]] = [
                pixels[px_base + dc, py_base + dr]  # type: ignore[index]
                for dr, dc in _DOT_POS
            ]
            cell_lums = [_luminance(r, g, b) for r, g, b in cell_pixels]

            # Per-cell threshold: local median of 8 pixels.
            # For exactly 8 values, the median is the average of indices 3 and 4
            # after sorting. Since we only need a threshold (not the sorted list),
            # we can use a 1-pass partial approach, but sorted() on 8 ints is
            # already very fast. The real win is the contrast gate below.
            if threshold is not None:
                cell_threshold = threshold# * 0.32
            else:
                # nth_element equivalent for 8 values: sort once, take [4]
                s = cell_lums[:]
                s.sort()
                median = s[4]
                
                # === LOCAL CONTRAST ADAPTIVE THRESHOLD ===
                contrast = s[7] - s[0]          # range of luminance in this cell
                
                if contrast < 35:               # flat area (skin, sky, clothing)
                    multiplier = 0.23           # lower threshold = more dots lit → softer, artistic
                elif contrast > 110:            # high contrast (eyes, hair, edges, jewelry)
                    multiplier = 0.52           # higher threshold = sharper detail
                else:
                    multiplier = 0.38           # balanced default

                cell_threshold = s[4] * multiplier

            braille_bits = 0
            lit_r: list[int] = []
            lit_g: list[int] = []
            lit_b: list[int] = []
            dark_r: list[int] = []
            dark_g: list[int] = []
            dark_b: list[int] = []

            for dot_idx, lum in enumerate(cell_lums):
                r, g, b = cell_pixels[dot_idx]
                if lum >= cell_threshold:
                    braille_bits |= _DOT_BITS[dot_idx]
                    lit_r.append(r); lit_g.append(g); lit_b.append(b)
                else:
                    dark_r.append(r); dark_g.append(g); dark_b.append(b)

            # Foreground = average colour of lit pixels (the braille dots)
            if lit_r:
                f_r = sum(lit_r) // len(lit_r)
                f_g = sum(lit_g) // len(lit_g)
                f_b = sum(lit_b) // len(lit_b)
            else:
                r, g, b = cell_pixels[0]
                f_r, f_g, f_b = r, g, b

            # Background = average colour of unlit pixels (space between dots)
            if dark_r:
                b_r = sum(dark_r) // len(dark_r)
                b_g = sum(dark_g) // len(dark_g)
                b_b = sum(dark_b) // len(dark_b)
            else:
                b_r = f_r // 3
                b_g = f_g // 3
                b_b = f_b // 3

            codepoint = chr(0x2800 + braille_bits)
            row_chars.append(
                f"\033[38;2;{f_r};{f_g};{f_b}m"
                f"\033[48;2;{b_r};{b_g};{b_b}m"
                f"{codepoint}"
            )

        lines.append("".join(row_chars) + RESET)

    return "\n".join(lines)


def render_asset(
    filename: str,
    assets_dir: Path,
    cols: int = 60,
    rows: int = 28,
) -> Optional[str]:
    """Resolve *filename* from *assets_dir* and return braille ANSI string,
    or ``None`` if the file cannot be found or opened.
    """
    try:
        from PIL import Image as PilImage  # noqa: PLC0415
    except ImportError:
        return None

    path = assets_dir / filename
    if not path.exists():
        for ext in (".jpeg", ".jpg", ".png", ".gif"):
            alt = path.with_suffix(ext)
            if alt.exists():
                path = alt
                break
        else:
            return None

    try:
        img = PilImage.open(path)
        return image_to_braille_ansi(img, cols=cols, rows=rows)
    except Exception:
        return None


def render_with_chafa(
    image_path: Path,
    cols: int = 38,
    rows: int = 20,
) -> Optional[str]:
    """Render *image_path* using the ``chafa`` binary (must be on PATH).

    Uses ``--format symbols --symbols braille`` so chafa's error-diffusion
    dithering drives the braille dot selection — better quality than the
    Python per-cell threshold renderer.  Output is truecolor ANSI compatible
    with Rich's Text.from_ansi() inside a Textual Static widget.

    Returns ``None`` if chafa is not installed, returns a non-zero exit code,
    or any other error occurs — callers fall back to image_to_braille_ansi().
    """
    import shutil
    import subprocess

    if not shutil.which("chafa"):
        return None

    try:
        result = subprocess.run(
            [
                "chafa",
                "--format", "symbols",
                #"--symbols", "braille+dot",          # dot-level detail on edges/faces
                "--fill", "vhalf+hhalf+block",  # quarter/half-blocks fill smooth areas
                "--dither", "none",
                "--size", f"{cols}x{rows}",
                "--stretch",
                "--colors", "full",
                "--color-space", "din99d",  # perceptually uniform — better gradients
                "--work", "9",              # max quality; runs in a worker so fine
                str(image_path),
            ],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
    except Exception:
        pass
    return None


# Cache whether chafa is available so shutil.which() is only called once.
_CHAFA_AVAILABLE: Optional[bool] = None


def chafa_available() -> bool:
    """Return True if the ``chafa`` binary is on PATH (result is cached)."""
    global _CHAFA_AVAILABLE
    if _CHAFA_AVAILABLE is None:
        import shutil
        _CHAFA_AVAILABLE = shutil.which("chafa") is not None
    return _CHAFA_AVAILABLE