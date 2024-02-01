from classes.DBConnector import DatabaseConnector


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
