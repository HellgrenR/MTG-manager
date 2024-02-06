from classes.DBConnector import DatabaseConnector
import pandas as pd
import matplotlib.pyplot as plt
from classes.decks import Decks


class Stats:  # Creating a class called Stats

    def __init__(self):  # Defining constructor
        self.db_connection = DatabaseConnector.connect()  # Calling connect static method
        self.decks = Decks()  # Creating an instance of Decks in Stats

    def deck_to_df(self, deck_name):  # Creating a method
        check = self.decks.check_deck_name(deck_name)  # Calling a method to check if deck_name exists
        deck = self.decks.get_all_from_deck(deck_name)  # Calling a method to get all cards from deck

        if check:  # If deck existed
            deck_df = pd.DataFrame(deck)  # Turning deck info into dataframe
            return deck_df  # Returning deck info as Dataframe
        else:  # If deck does not exist
            print("Deck not found")  # Print deck not found
            return None  # Returning none

    def view_mana_curve(self, deck_name):  # Creating a method
        deck = self.deck_to_df(deck_name)  # Calling deck_to_df method

        if deck is not None:  # Check if deck was found
            mana_cost_counts = deck.groupby("mana_cost").size().reset_index(
                name="count")  # Creating a table of the manacosts
            mana_cost_counts.plot(kind="bar", x="mana_cost", y="count", legend=False)  # Turning table into a diagram
            plt.xlabel("Mana Cost")  # Naming X axle
            plt.ylabel("Count")  # Naming Y axle
            plt.title("Mana Cost Distribution")  # Giving the diagram a title
            plt.show()  # Displaying the diagram

    def view_mana_blend(self, deck_name):  # Creating a method
        deck = self.deck_to_df(deck_name)  # Calling deck_to_df method

        if deck is not None:  # Check if deck was found
            mana_blend = deck[["white", "blue", "black", "red", "green"]].sum()  # Creating a table of the mana colors
            print(mana_blend)  # Printing it as a table

            colors = ["#fff700", "#0000FF", "#000000", "#FF0000", "#008000"]  # Defining colors for a pie chart
            mana_blend.plot.pie(startangle=90, legend=False, colors=colors,
                                autopct="%1.1f")  # Turning table into a pie chart
            plt.show()  # Displaying the pie chart
