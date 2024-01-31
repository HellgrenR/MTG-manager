from DBConnector import DatabaseConnector
from cards import Cards

choice = input("1. View cards\n"
               "2. View decks\n"
               "3. Add cards\n"
               "4. Add decks\n"
               "Q. quit\n"
               "Enter your choice: ").lower().strip()

cards = Cards()

match choice:
    case "1":
        print(cards.view_cards())
    case "2":
        print(cards.view_decks())

