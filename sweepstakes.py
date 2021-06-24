from user_interface import UserInterface
from contestant import Contestant


class Sweepstakes:
        def __init__(self):
            self.name = UserInterface.get_user_string("Enter the name of your sweepstakes here.")
            self.contestants = {}

        def register_contestant(self, contestant):
            contestant.registration_number = len(self.contestants)
            self.contestants.update({len(self.contestants): contestant})
            pass

        def show_contestant(self):
            pass

        def choose_winner(self):
            pass

        def menu(self):
            UserInterface.display_sweepstakes_menu_choices()
            user_selection = UserInterface.get_user_int("Enter the number that corresponds with your choice")
            if user_selection == 1:
                Sweepstakes.register_contestant(Contestant())
            elif user_selection == 2:
                Sweepstakes.choose_winner("")
            elif user_selection == 3:
                Sweepstakes.show_contestant("")
            else:
                pass


