from classes.cards import Cards


class CardMenu:
    def __init__(self):
        self.choice = input("\n1. View cards"
                            "\n2. Add cards"
                            "\n3. Delete cards"
                            "\nR. return to main menu"
                            "\nEnter your choice: ").lower().strip()

        self.cards = Cards()

        match self.choice:
            case "1":  # View cards
                print(self.cards.view_cards())

            case "2":  # Add cards
                while True:
                    card_name = input("\nEnter card name "
                                      "\n!r to return: ").lower().strip()
                    if card_name == "!r":
                        print("Returning")
                        break
                    else:
                        self.cards.add_card(card_name)

            case "3":  # Delete cards
                pass

            case "r":  # Return to main menu
                pass

            case _:
                print("Invalid input")
