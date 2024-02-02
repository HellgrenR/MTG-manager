from classes.cards import Cards
from menus.card_menu import CardMenu
from menus.deck_creation import DeckCreation


class MainMenu:
    def __init__(self):
        self.choice = input("\n1. Card options"
                       "\n2. View decks"
                       "\nQ. quit"
                       "\nEnter your choice: ").lower().strip()

        match self.choice:
            case "1":  # Card options
                cards = CardMenu()

            case "2":  # Deck options
                decks = DeckCreation()

            case "q":  # quit
                pass

            case _:
                print("Invalid input")

