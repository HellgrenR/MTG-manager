from classes.decks import Decks
import pandas as pd


class DeckCreation:

    def __init__(self):

        self.decks = Decks()

        while True:
            self.choice = input("\n================================="
                                "\n           DECKS MENU"
                                "\n================================="
                                "\n1. Create empty deck"
                                "\n2. View decks"
                                "\n3. View deck contents"
                                "\n4. Add cards to deck"
                                "\n5. Delete cards from deck"
                                "\n6. Delete decks"
                                "\nR. Return to main menu"
                                "\nEnter your choice: ").lower().strip()

            match self.choice:
                case "1":  # Create empty deck
                    deck_name = input("\nEnter deck name: ")
                    deck_description = input("Enter deck description: ")
                    self.decks.create_deck(deck_name, deck_description)

                case "2":  # View decks
                    decks = self.decks.view_decks()
                    decks_df = pd.DataFrame(decks)
                    print("\nDecks: \n", decks_df)

                case "3":  # view deck contents
                    deck_name = input("\nEnter deck name: ")

                    check = self.decks.check_deck_name(deck_name)

                    if check:
                        contents = self.decks.view_contents(deck_name)
                        contents_df = pd.DataFrame(contents, columns=["Cards"])
                        contents_df.sort_values(by="Cards", ascending=True, inplace=True)

                        print("\nDeck contents: \n", contents_df)

                case "4":  # add cards to deck
                    deck_name = input("\nEnter deck name: ")
                    self.decks.add_new_to_deck(deck_name)

                case "5":  # delete cards from deck
                    deck_name = input("\nEnter deck name: ")

                    check = self.decks.check_deck_name(deck_name)
                    if check:
                        card_name = input("\nEnter card name: ")
                        self.decks.delete_card_from_deck(card_name, deck_name)

                case "6":  # delete entire decks
                    deck_name = input("\nEnter deck name: ")

                    self.decks.delete_deck(deck_name)

                case "r":  # return to main_menu
                    return

                case _:
                    print("Invalid input")

