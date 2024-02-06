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
                           "\nr. Return to main menu")

            match choice:
                case "1":  # View mana curve
                    deck_name = input("\nEnter deck name: ")
                    self.stats.view_mana_curve(deck_name)

                case "2":  # View color mix
                    deck_name = input("\nEnter deck name: ")
                    self.stats.view_mana_blend(deck_name)


                case "r":
                    return

