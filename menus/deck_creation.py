from classes.decks import Decks
from classes.cards import Cards


class DeckCreation:

    def __init__(self):

        self.decks = Decks()

        while True:
            self.choice = input("\n1. Create empty deck"
                                "\n2. View decks"
                                "\n3. Add existing cards to deck"
                                "\n4. Add new cards to deck"
                                "\n5. Delete cards from deck"
                                "\n6. Delete decks"
                                "\nR. Return to main menu"
                                "\n Enter your choice: ").lower().strip()

            match self.choice:
                case "1":  # Create empty deck
                    deck_name = input("\nEnter deck name: ")
                    deck_description = input("Enter deck description: ")
                    self.decks.create_deck(deck_name, deck_description)

                case "2":  # View decks
                    print(self.decks.view_decks())

                case "3":  # add existing cards to deck
                    deck_name = input("\nEnter deck name: ")
                    card_list = []

                    while True:
                        card_name = input("!f to finish"
                                          "\nEnter card name: ").lower()
                        if card_name == "!f":
                            break
                        else:
                            card_list.append(card_name)

                    self.decks.add_existing_to_deck(deck_name, card_list)

                case "4":  # add new cards to deck
                    deck_name = input("\nEnter deck name: ")

                    self.decks.add_to_deck_new(deck_name)

                case "5":  # delete cards from deck
                    pass

                case "6":  # delete entire decks
                    deck_name = input("\nEnter deck name: ")

                    self.decks.delete_deck(deck_name)

                case "r":  # return to main_menu
                    return

                case _:
                    print("Invalid input")

