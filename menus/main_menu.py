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
                while True:
                    card_name = input("\nEnter card name "
                                      "\n!r to return: ").lower().strip()
                    if card_name == "!r":
                        print("Returning")
                        break
                    else:
                        cards.add_card(card_name)

            case "4":
                decks = DeckCreation()
                decks.menu()
