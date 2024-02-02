from classes.decks import Decks

class DeckCreation:

    def menu(self):
        choice = input("\n1. Use new cards"
                         "\n2. Use existing cards"
                         "\nR. Return to main menu"
                         "\n Enter your choice: ").lower().strip()

        decks = Decks()

        match choice:
            case "1":
                deck_name = input("Enter deck name: ")
                deck_description = input("Enter deck description: ")
                decks.create_deck(deck_name, deck_description)


