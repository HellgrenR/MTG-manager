from classes.cards import Cards


class MainMenu:
    choice = input("\n1. View cards"
                   "\n2. View decks"
                   "\n3. Add cards"
                   "\n4. Add decks"
                   "\nQ. quit"
                   "\nEnter your choice: ").lower().strip()

    cards = Cards()

    match choice:
        case "1":
            print(cards.view_cards())

        case "2":
            print(cards.view_decks())

        case "3":
            card_name = input("\nEnter card name (Make sure you spell it correctly): ")
            cards.add_card(card_name)

        case "4":

