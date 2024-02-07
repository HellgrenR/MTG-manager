from classes.stats import Stats


class StatMenu:

    def __init__(self):

        self.stats = Stats()

        while True:
            choice = input("\n================================="
                           "\n           STATS MENU"
                           "\n================================="
                           "\n1. View deck mana curve"
                           "\n2. View deck color mix"
                           "\nR. Return to main menu"
                           "\nEnter your choice: ").lower().strip()

            match choice:
                case "1":  # View mana curve
                    deck_name = input("\nEnter deck name: ")  # Input for deck name
                    self.stats.view_mana_curve(deck_name)  # Calling view_mana_curve method

                case "2":  # View color mix
                    deck_name = input("\nEnter deck name: ")  # Input for deck name
                    self.stats.view_mana_blend(deck_name)  # Calling view_mana_blend

                case "r":
                    return  # Return to main menu

                case _:
                    print("Invalid input")  # Print for wrong input
