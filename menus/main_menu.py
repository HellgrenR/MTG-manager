from menus.card_menu import CardMenu
from menus.deck_creation import DeckCreation
from menus.stat_menu import StatMenu


class MainMenu:
    def __init__(self):
        while True:
            self.choice = input("\n================================="
                                "\n           MAIN MENU"
                                "\n================================="
                                "\n1. Card options"
                                "\n2. View decks"
                                "\n3. View statistics"
                                "\nQ. quit"
                                "\nEnter your choice: ").lower().strip()

            match self.choice:
                case "1":  # Card options
                    cards = CardMenu()

                case "2":  # Deck options
                    decks = DeckCreation()

                case "3":
                    stats = StatMenu()

                case "q":  # quit
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid input")


