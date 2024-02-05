from classes.DBConnector import DatabaseConnector


class Stats:

    def __init__(self):
        self.db_connection = DatabaseConnector.connect()


