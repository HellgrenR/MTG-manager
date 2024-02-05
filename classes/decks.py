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

    def view_contents(self, deck_name):
        cursor = self.db_connection.cursor(dictionary=True)

        # Get the deck ID
        query_deck_id = "SELECT id FROM Decks WHERE name = %s"
        cursor.execute(query_deck_id, (deck_name,))
        deck_id_result = cursor.fetchone()

        if not deck_id_result:
            print(f"Deck '{deck_name}' not found.")
            return None

        deck_id = deck_id_result["id"]

        # Select card IDs associated with the deck from the CardDeck table
        query_card_ids = "SELECT card_id FROM CardDeck WHERE deck_id = %s"
        cursor.execute(query_card_ids, (deck_id,))
        card_ids_result = cursor.fetchall()

        if not card_ids_result:
            print(f"No cards found in deck '{deck_name}'.")
            return None

        # Get card names associated with the retrieved card IDs
        card_names = []
        for card_id_result in card_ids_result:
            card_id = card_id_result["card_id"]
            query_card_name = "SELECT name FROM Cards WHERE id = %s"
            cursor.execute(query_card_name, (card_id,))
            card_name_result = cursor.fetchone()

            if card_name_result:
                card_names.append(card_name_result["name"])

        return card_names

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

        self.add_existing_to_deck(deck_name, card_list)

    def add_existing_to_deck(self, deck_name, card_list):
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

    def delete_deck(self, deck_name):
        cursor = self.db_connection.cursor(dictionary=True)

        subquery = "SELECT id FROM Decks WHERE name = %s"
        query = f"DELETE FROM CardDeck WHERE deck_id IN ({subquery})"

        cursor.execute(query, (deck_name,))
        result = self.db_connection.commit()

        query = "DELETE FROM Decks WHERE name = %s"
        cursor.execute(query, (deck_name,))
        result2 = self.db_connection.commit()

        print(f"Deleted deck {deck_name}")

        return result, result2

    def delete_card_from_deck(self, card_name, deck_name):
        cursor = self.db_connection.cursor(dictionary=True)

        # Get all card IDs with the given name
        query_card_ids = "SELECT id FROM Cards WHERE name = %s"
        cursor.execute(query_card_ids, (card_name,))
        card_ids_result = cursor.fetchall()

        if not card_ids_result:
            print(f"No cards found with the name '{card_name}'.")
            return None

        # Get the deck ID
        query_deck_id = "SELECT id FROM Decks WHERE name = %s"
        cursor.execute(query_deck_id, (deck_name,))
        deck_id_result = cursor.fetchone()

        if not deck_id_result:
            print(f"Deck '{deck_name}' not found.")
            return None

        deck_id = deck_id_result["id"]

        # Delete each card with the given name from the CardDeck table
        for card_id_result in card_ids_result:
            card_id = card_id_result["id"]
            query_delete_card = "DELETE FROM CardDeck WHERE card_id = %s AND deck_id = %s"
            cursor.execute(query_delete_card, (card_id, deck_id))

        result = self.db_connection.commit()

        if result:
            print(f"Deleted all cards with the name '{card_name}' from '{deck_name}'.")
        else:
            print(f"Failed to delete cards with the name '{card_name}' from '{deck_name}'.")

        return result
