import random
from user_interface import UserInterface
from contestant import Contestant


class Sweepstakes:
    contestants = {}

    def __init__(self):
        self.name = UserInterface.get_user_string("Enter the name of your sweepstakes here.")

    def register_contestant(self, contestant):
        contestant.registration_number = len(self.contestants)
        self.contestants.update({len(self.contestants): contestant})

    def show_contestant(self):
        UserInterface.display_message(self.contestants.items())

    def choose_winner(self):
        return random.choice(list(self.contestants))

    def menu(self):
        UserInterface.display_sweepstakes_menu_choices()
        user_selection = UserInterface.get_user_int("Enter the number that corresponds with your choice")
        if user_selection == 1:
            self.register_contestant()
        elif user_selection == 2:
            self.choose_winner()
        elif user_selection == 3:
            self.show_contestant()
        else:
            UserInterface.get_user_int(" Not Valid entry. Try again")
