from classes.cards import Cards
from classes.decks import Decks
from menus.deck_creation import DeckCreation


class MainMenu:
    def __init__(self):
        self.choice = input("\n1. Card options"
                       "\n2. View decks"
                       "\nQ. quit"
                       "\nEnter your choice: ").lower().strip()

        cards = Cards()

        match self.choice:
            case "1":  # Card options
                print(cards.view_cards())

            case "2":  # Deck options
                decks = DeckCreation()
                decks.menu()

            case "q":  # quit
                pass

            case _:
                print("Invalid input")

