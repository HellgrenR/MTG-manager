import mysql.connector


class DatabaseConnector:

    @staticmethod
    def connect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="mypassword",
            database="MTG-manager"
        )

