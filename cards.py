from mtgsdk import Card
from DBConnector import DatabaseConnector

# Example: Search for a card by name
card_name = "Wrath of god"
cards = Card.where(name=card_name).all()

print(cards[0])

# Print card details
print(vars(cards[0]))

class Cards:
    def __init__(self):
        self.cards = []
        self.db_connection = DatabaseConnector.connect()

    def view_cards(self):
        cursor = self.db_connection.cursor()

        query = "SELECT * FROM Cards"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def view_decks(self):
        cursor = self.db_connection.cursor()

        query = "SELECT * FROM Decks"
        cursor.execute(query)
        result = cursor.fetchall()

        return result
