from classes.DBConnector import DatabaseConnector
import pandas as pd
import matplotlib.pyplot as plt
from classes.decks import Decks


class Stats:

    def __init__(self):
        self.db_connection = DatabaseConnector.connect()
        self.decks = Decks()

    def deck_to_df(self, deck_name):
        deck = self.decks.get_all_from_deck(deck_name)

        deck_df = pd.DataFrame(deck)

        return deck_df

    def view_mana_curve(self, deck_name):
        deck = self.deck_to_df(deck_name)

        print(deck)
