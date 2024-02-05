from classes.stats import Stats


class StatMenu:

    def __init__(self):

        self.stats = Stats()

        choice = input("\n================================="
                       "\n           STATS MENU"
                       "\n================================="
                       "\n1. View deck mana curve"
                       "\n2. View deck color mix")

        match choice:
            case "1":  # View mana curve
                pass


