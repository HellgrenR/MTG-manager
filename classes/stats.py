from classes.DBConnector import DatabaseConnector
import pandas as pd
import matplotlib.pyplot as plt
from classes.decks import Decks


class Stats:

    def __init__(self):
        self.db_connection = DatabaseConnector.connect()
        self.decks = Decks()

    def deck_to_df(self, deck_name):
        self.decks.check_deck_name(deck_name)
        deck = self.decks.get_all_from_deck(deck_name)

        deck_df = pd.DataFrame(deck)

        return deck_df

    def view_mana_curve(self, deck_name):
        deck = self.deck_to_df(deck_name)

        mana_cost_counts = deck.groupby("mana_cost").size().reset_index(name="count")
        mana_cost_counts.plot(kind="bar", x="mana_cost", y="count", legend=False)
        plt.xlabel("Mana Cost")
        plt.ylabel("Count")
        plt.title("Mana Cost Distribution")
        plt.show()

    def view_mana_blend(self, deck_name):
        deck = self.deck_to_df(deck_name)

        mana_blend = deck[["white", "blue", "black", "red", "green"]].sum()
        print(mana_blend)

        colors = ["#fff700", "#0000FF", "#000000", "#FF0000", "#008000"]

        # Plotting a pie chart without legend
        ax = mana_blend.plot.pie(startangle=90, legend=False, colors=colors)

        # Display the pie chart
        plt.show()



