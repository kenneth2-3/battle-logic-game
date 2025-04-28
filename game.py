import string
from board import Board
from colorama import Fore, init

init(autoreset=True)  # This automatically resets the color after each print


def parse_input(user_input, size):
    """
    Parses the user's input (e.g., 'A3') into grid coordinates.

    Args:
        user_input (str): The guess entered by the player.
        size (int): The size of the game grid.

    Returns:
        tuple: (row, col) coordinates if valid, or None if input is invalid.
    """
    try:
        col = string.ascii_uppercase.index(user_input[0].upper())
        row = int(user_input[1:]) - 1
        if row < 0 or col >= size:
            raise ValueError("Out of bounds")
        return row, col
    except (ValueError, IndexError):
        return None
