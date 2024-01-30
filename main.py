import DBConnector
from mtgsdk import Card

# Example: Search for a card by name
card_name = "Wrath of god"
cards = Card.where(name=card_name).all()

print(cards[0])

# Print card details
print(vars(cards[0]))


choice = input("1. View cards\n"
               "2. View decks\n"
               "3. Add cards\n"
               "4. Add decks\n"
               "Q. quit\n"
               "Enter your choice: ")

