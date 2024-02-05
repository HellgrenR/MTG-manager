from classes.cards import Cards
from menus.card_menu import CardMenu
from menus.deck_creation import DeckCreation


class MainMenu:
    def __init__(self):
        while True:
            self.choice = input("\n================================="
                                "\n           MAIN MENU"
                                "\n================================="
                                "\n1. Card options"
                                "\n2. View decks"
                                "\nQ. quit"
                                "\nEnter your choice: ").lower().strip()

            match self.choice:
                case "1":  # Card options
                    cards = CardMenu()

                case "2":  # Deck options
                    decks = DeckCreation()

                case "q":  # quit
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid input")


