import random


class Board:
    """A class representing the Battleships game board."""

    def __init__(self, size):
        """
        Initialize the game board with a given size.

        Args(Argument):
            size (int): Size of the board (number of rows and columns).
        """
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.missed_guesses = []  # To track missed guesses

    def print_board(self, reveal_ships=False):
        """
        Print the current state of the board.

        Args:
            reveal_ships (bool): If True, shows all ships;
            otherwise hides ships.
        """
        # Print column labels
        print("  ", end="")
        for col in range(self.size):
            print(chr(65 + col), end=" ")
        print()

        # Print rows with row numbers
        for row in range(self.size):
            print(f"{row + 1:2} ", end="")
            for col in range(self.size):
                if reveal_ships:
                    print(self.grid[row][col], end=" ")
                else:
                    cell_value = self.grid[row][col]
                    if cell_value == 'S':
                        print('X', end=" ")  # To hide ships during the game
                    else:
                        print(cell_value, end=" ")
            print()