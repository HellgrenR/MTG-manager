from mtgsdk import Card
from classes.DBConnector import DatabaseConnector
import mysql.connector


class Cards:
    def __init__(self):
        self.cards = []

    def view_cards(self):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

        query = "SELECT name FROM Cards"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def remove_card(self, card_name):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True)

        subquery = ("SELECT 1 FROM CardDeck "
                    "WHERE CardDeck.card_id = Cards.id LIMIT 1")

        # Delete the card only if it's not in CardDeck
        query = f"DELETE FROM Cards WHERE Cards.name = %s AND NOT EXISTS ({subquery}) LIMIT 1"

        cursor.execute(query, (card_name,))
        result = db_connection.commit()
        print(f"Removed {card_name}")
        print(result)

    def add_card(self, card_name):
        cards = Card.where(name=card_name).all()

        for card in cards:
            while True:
                choice = input(f"Is {card.name} the correct card? (y/n)").lower().strip()

                if choice == "y":
                    card = self.find_and_add_card(card)
                    return card
                elif choice == "n":
                    break
                else:
                    print("Invalid choice. Please enter 'y' or 'n'.")
                    continue

    def find_and_add_card(self, card):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True, buffered=True)

        query = "SELECT * FROM Cards WHERE name = %s"
        cursor.execute(query, (card.name,))
        result = cursor.fetchone()

        if result is None:
            self.add_to_db(card)
        else:
            print(f"Found {card.name} in database")
            return card

    def add_to_db(self, card):
        db_connection = DatabaseConnector.connect()
        cursor = db_connection.cursor(dictionary=True, buffered=True)

        colors = {
            "white": 0,
            "blue": 0,
            "black": 0,
            "red": 0,
            "green": 0,
            "NonType": 0
        }

        if card.colors is not None:
            for color in card.colors:
                match color:
                    case "W":
                        colors["white"] += 1
                    case "U":
                        colors["blue"] += 1
                    case "B":
                        colors["black"] += 1
                    case "R":
                        colors["red"] += 1
                    case "G":
                        colors["green"] += 1

        query = """INSERT INTO Cards 
                    (name, mana_cost, type, rarity, text, image_url, white, blue, black, red, green, power, toughness) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(query, (card.name,
                                   card.cmc,
                                   card.type,
                                   card.rarity,
                                   card.text,
                                   card.image_url,
                                   colors["white"],
                                   colors["blue"],
                                   colors["black"],
                                   colors["red"],
                                   colors["green"],
                                   card.power,
                                   card.toughness))
            db_connection.commit()

            print(f"Added {card.name} to database")
            return card

        except mysql.connector.Error as err:
            print(f"Error while connecting to MySQL: {err}")
        finally:
            cursor.close()
