import mysql.connector


class DatabaseConnector:  # Creating a class called DatabaseConnector

    @staticmethod  # Making it a static method so that I don't have to declare class when I use it
    def connect():  # Declaring a method
        return mysql.connector.connect(  # Return connection to database
            host="localhost",  # Hosts name
            user="root",  # User name
            password="mypassword",  # User password
            database="MTG-manager"  # Schema name
        )

