from classes.DBConnector import DatabaseConnector
from classes.cards import Cards


class Decks:
    def __init__(self):
        self.db_connection = DatabaseConnector.connect()

    def view_decks(self):
        cursor = self.db_connection.cursor()

        query = "SELECT * FROM Decks"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def create_deck(self, deck_name, deck_description):
        cursor = self.db_connection.cursor()

        query = "INSERT INTO Decks (name, description) VALUES (%s, %s)"
        cursor.execute(query, (deck_name, deck_description))
        result = self.db_connection.commit()
        print("Deck created successfully")
        return result  # Add error handling

    def add_to_deck_new(self, deck_name):
        cards = Cards()
        card_list = []

        while True:
            card_name = input("\nEnter card name\n!r to return: ").lower().strip()
            if card_name == "!r":
                print("Returning")
                break
            else:
                card = cards.add_card(card_name)
                card_list.append(card)

        cursor = self.db_connection.cursor(dictionary=True)

        query = "SELECT * FROM Decks WHERE name = %s"
        cursor.execute(query, (deck_name,))
        deck = cursor.fetchone()

        if deck:
            # If the deck exists, add cards to the CardDeck table
            for card in card_list:
                # Fetch the card from the Cards table
                query_card = "SELECT * FROM Cards WHERE name = %s"
                cursor.execute(query_card, (card.name,))
                fetched_card = cursor.fetchall()[0]  # Read the result set

                # Insert into CardDeck
                query_insert = "INSERT INTO CardDeck (card_id, deck_id) VALUES (%s, %s)"
                cursor.execute(query_insert, (fetched_card["id"], deck["id"]))

            result = self.db_connection.commit()
            print(f"Added cards to {deck['name']}")
            return result
        else:
            print(f"Deck with name {deck_name} not found.")
            return None

