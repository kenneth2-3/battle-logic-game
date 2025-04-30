from game import start_game
from simple_term_menu import TerminalMenu


def main():
    while True:
        start_game()
        options = ["Play Again", "Exit"]
        terminal_menu = TerminalMenu(
            options,
            title="What would you like to do next?"
        )
        choice = terminal_menu.show()

        if options[choice] == "Exit":
            print("Thanks for playing Battleships! Goodbye.")
            break


if __name__ == "__main__":
    main()
