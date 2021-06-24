import user_interface
from contestant import Contestant
from marketing_firm import MarketingFirm
import random

class Sweepstakes:

    def __init__(self, person_name, every_contestant ):
        self.name = person_name
        self.contestants = every_contestant

        def register_contestant(contestant):
            self.contestants.append(contestant)

        def choose_winner():
            chicken_dinner = random.randint(self.contestants)
            Contestant.notify_winner_status()
            return notify_winner_status

        def show_contestant():
            return user_interface.UserInterface.display_contestant_info()

    def menu(self):
        user_interface.UserInterface.display_sweepstakes_menu_choices()
        user_selection = user_interface.UserInterface.get_user_int("Enter your Choice's Corresponding Number")
        if user_selection == 1:
            if user_selection == 1:
                Sweepstakes.register_contestant(Contestant())
            elif user_selection == 2:
                Sweepstakes.choose_winner("")
            elif user_selection == 3:
                Sweepstakes.view_contestant("")
            else:



