from user_interface import UserInterface
from contestant import Contestant


class Sweepstakes:

    def __init__(self):
        self.name = ""
        self.contestants = {}

        def register_contestant(contestant):
            pass

        def choose_winner():

            pass

        def show_contestant():
            pass

    def menu(self):
        UserInterface.display_sweepstakes_menu_choices()
        user_selection = UserInterface.get_user_int("Enter your Choice's Corresponding Number")
        if user_selection == 1:
            Sweepstakes.register_contestant()
        elif user_selection == 2:
            Sweepstakes.choose_winner()
        elif user_selection == 3:
            Sweepstakes.show_contestant()
        else:



