import user_interface
from contestant import Contestant
import random

class Sweepstakes:

    def __init__(self):
        self.name = ""
        self.contestants = {}

        def register_contestant(contestant):
            contestant.registration_number = len(self.contestants)
            self.contestants.update({len(self.contestants): contestant})

        def choose_winner():
            return random.choice(list(self.contestants))
            pass

        def show_contestant():
            user_interface.display_message(self.contestants.items())
            pass

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



