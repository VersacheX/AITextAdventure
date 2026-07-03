"""
Rendering utilities for TUI elements.

Provides consistent box drawing, text formatting, and layout helpers.
"""
import os
from typing import List, Optional


def clear_screen() -> None:
    """Clear the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def make_border(width: int, char: str = '*') -> str:
    """Create a border line of the specified width."""
    return char * width


def make_box(content: List[str], width: int, border_char: str = '*', 
             center_content: bool = False) -> List[str]:
    """
    Create a framed box around content.

    Args:
        content: Lines of text to frame
        width: Total width including borders
        border_char: Character to use for borders
        center_content: Whether to center content within box

    Returns:
        List of framed lines including borders
    """
    inner_width = max(0, width - 4)
    border = make_border(width, border_char)
    lines = [border]

    for line in content:
        if center_content:
            padded = line.center(inner_width)[:inner_width]
        else:
            padded = line.ljust(inner_width)[:inner_width]
        lines.append(f"{border_char} {padded} {border_char}")

    lines.append(border)
    return lines


def wrap_text(text: str, width: int) -> List[str]:
    """
    Wrap text to fit within the specified width.

    Args:
        text: Text to wrap
        width: Maximum line width

    Returns:
        List of wrapped lines
    """
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            if current_line:
                current_line += " "
            current_line += word
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def make_dialog_box(text: str, width: int) -> List[str]:
    """
    Create a dialog box with wrapped text.

    Args:
        text: Dialog text
        width: Box width

    Returns:
        List of framed dialog lines
    """
    wrapped = wrap_text(text, width - 4)
    return make_box(wrapped, width)


def highlight_box(lines: List[str], highlight_char: str = '#') -> List[str]:
    """
    Replace border characters with highlight characters.

    Args:
        lines: Box lines to highlight
        highlight_char: Character to use for highlighting

    Returns:
        Highlighted box lines
    """
    return [line.replace('*', highlight_char) for line in lines]


def center_box_in_terminal(box_lines: List[str]) -> List[str]:
    """
    Add padding to center a box horizontally in the terminal.

    Args:
        box_lines: Box lines to center

    Returns:
        Centered box lines with padding
    """
    try:
        term_width = os.get_terminal_size().columns
    except OSError:
        term_width = 80

    box_width = len(box_lines[0]) if box_lines else 0
    padding = max(0, (term_width - box_width) // 2)

    return [' ' * padding + line for line in box_lines]