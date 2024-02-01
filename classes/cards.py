from mtgsdk import Card
from classes.DBConnector import DatabaseConnector
import mysql.connector


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

    def add_card(self, card_name):
        cards = Card.where(name=card_name).all()
        card = cards[0]

        choice = input(f"Is this {card} the correct card? (y/n)")

        if choice == "n":
            return False
        elif choice == "y":
            colors = {
                "white": 0,
                "blue": 0,
                "black": 0,
                "red": 0,
                "green": 0
            }

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

            cursor = self.db_connection.cursor()

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
                self.db_connection.commit()

                print(f"Added {card.name}")

            except mysql.connector.Error as err:
                print(f"Error while connecting to MySQL: {err}")
            finally:
                cursor.close()
