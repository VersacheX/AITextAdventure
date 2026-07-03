"""
Input handling utilities for consistent keyboard interaction.
"""
from typing import Optional, Callable
from readchar import readkey, key


class InputHandler:
    """
    Handles keyboard input with support for single-key and text input.
    """

    @staticmethod
    def get_key(prompt: str = "") -> str:
        """
        Read a single keypress.

        Args:
            prompt: Optional prompt to display

        Returns:
            Key string (normalized for arrow keys and special keys)
        """
        if prompt:
            print(prompt, end='', flush=True)

        ch = readkey()

        # Normalize arrow keys
        if ch == key.UP:
            return 'up'
        elif ch == key.DOWN:
            return 'down'
        elif ch == key.LEFT:
            return 'left'
        elif ch == key.RIGHT:
            return 'right'
        elif ch == key.ESC:
            return 'esc'
        elif ch == key.ENTER:
            return 'enter'

        return ch.lower()

    @staticmethod
    def get_text(prompt: str = "", validator: Optional[Callable[[str], bool]] = None) -> str:
        """
        Read a line of text input with optional validation.

        Args:
            prompt: Prompt to display
            validator: Optional validation function

        Returns:
            Validated input string
        """
        while True:
            text = input(prompt).strip()

            if validator is None or validator(text):
                return text

            print("Invalid input. Please try again.")

    @staticmethod
    def get_number(prompt: str = "", min_val: Optional[int] = None, 
                   max_val: Optional[int] = None) -> int:
        """
        Read a numeric input with optional range validation.

        Args:
            prompt: Prompt to display
            min_val: Minimum allowed value
            max_val: Maximum allowed value

        Returns:
            Validated integer
        """
        def validator(text: str) -> bool:
            if not text.isdigit():
                return False
            val = int(text)
            if min_val is not None and val < min_val:
                return False
            if max_val is not None and val > max_val:
                return False
            return True

        text = InputHandler.get_text(prompt, validator)
        return int(text)

    @staticmethod
    def get_confirmation(prompt: str = "Are you sure? (y/n): ") -> bool:
        """
        Get yes/no confirmation.

        Args:
            prompt: Confirmation prompt

        Returns:
            True for yes, False for no
        """
        while True:
            ch = InputHandler.get_key(prompt)
            if ch == 'y':
                return True
            elif ch == 'n':
                return False