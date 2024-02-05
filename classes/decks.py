from classes.DBConnector import DatabaseConnector
from classes.cards import Cards
import mysql.connector


class Decks:
    def __init__(self):
        pass
    def check_deck_name(self, deck_name):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

        try:
            query = "SELECT * FROM Decks WHERE name = %s"
            cursor.execute(query, (deck_name,))
            result = cursor.fetchall()
            cursor.close()

            if result:
                print(f"Deck with name {deck_name} exists.")
                return result
            else:
                print(f"Deck with name {deck_name} not found.")
                return False

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def view_decks(self):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

        query = "SELECT * FROM Decks"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def get_all_from_deck(self, deck_name):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

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
        cards = []
        for card_id_result in card_ids_result:
            card_id = card_id_result["card_id"]
            query_cards = "SELECT * FROM Cards WHERE id = %s"
            cursor.execute(query_cards, (card_id,))
            card_result = cursor.fetchone()

            if card_result:
                cards.append(card_result)

        return cards

    def view_contents(self, deck_name):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

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
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

        query = "INSERT INTO Decks (name, description) VALUES (%s, %s)"
        cursor.execute(query, (deck_name, deck_description))
        result = db_connection.commit()
        print("Deck created successfully")
        return result  # Add error handling

    def add_new_to_deck(self, deck_name):
        deck = self.check_deck_name(deck_name)
        cards = Cards()

        while True:
            card_name = input("\nEnter card name\n!r to return: ").lower().strip()
            if card_name == "!r":
                print("Returning")
                break
            else:
                card = cards.add_card(card_name)
                self.add_card_to_deck(deck, card)

    def add_card_to_deck(self, deck, card):
        updated_db = DatabaseConnector.connect()
        cursor = updated_db.cursor(dictionary=True)

        try:
            deck = deck[0]
            card_name = card.name
            print(f"Adding card '{card_name}' to deck '{deck['name']}'")

            # Retrieve card ID using subquery
            subquery = "SELECT id FROM Cards WHERE name = %s LIMIT 1"
            cursor.execute(subquery, (card_name,))
            card_result = cursor.fetchone()
            print(card_result)

            if card_result:
                card_id = card_result["id"]
                print("cardID: ", card_id)
                print("DeckID: ", deck["id"])

                # Insert card into CardDeck table
                query = "INSERT INTO CardDeck (card_id, deck_id) VALUES (%s, %s)"
                cursor.execute(query, (card_id, deck["id"]))
                try:
                    updated_db.commit()
                    print("Commit successful")
                except mysql.connector.Error as commit_err:
                    print(f"Error during commit: {commit_err}")
            else:
                print(f"Card '{card_name}' not found.")
        except mysql.connector.Error as err:
            print(f"Error adding card to deck: {err}")
        finally:
            cursor.close()

    def delete_deck(self, deck_name):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

        subquery = "SELECT id FROM Decks WHERE name = %s"
        query = f"DELETE FROM CardDeck WHERE deck_id IN ({subquery})"

        cursor.execute(query, (deck_name,))
        result = DatabaseConnector.connect().commit()

        query = "DELETE FROM Decks WHERE name = %s"
        cursor.execute(query, (deck_name,))
        result2 = db_connection.commit()

        print(f"Deleted deck {deck_name}")

        return result, result2

    def delete_card_from_deck(self, card_name, deck_name):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

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

        result = db_connection.commit()

        if result:
            print(f"Deleted all cards with the name '{card_name}' from '{deck_name}'.")
        else:
            print(f"Failed to delete cards with the name '{card_name}' from '{deck_name}'.")

        return result
