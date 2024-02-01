from classes.cards import Cards
from classes.decks import Decks
from menus.deck_creation import DeckCreation


class MainMenu:
    def __init__(self):
        self.choice = input("\n1. View cards"
                       "\n2. View decks"
                       "\n3. Add cards"
                       "\n4. Add decks"
                       "\nQ. quit"
                       "\nEnter your choice: ").lower().strip()

        cards = Cards()
        decks = Decks()

        match self.choice:
            case "1":
                print(cards.view_cards())

            case "2":
                print(decks.view_decks())

            case "3":
                card_name = input("\nEnter card name (Make sure you spell it correctly): ")
                cards.add_card(card_name)

            case "4":
                decks = DeckCreation()
                decks.menu()
