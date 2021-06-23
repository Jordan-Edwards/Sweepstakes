from user_interface import UserInterface
from sweepstakes import Sweepstakes


class Contestant:

    def __init__(self):
        self.first_name = UserInterface.get_user_string("Enter your Legal First Name")
        self.last_name = UserInterface.get_user_string("Enter your Legal Last Name")
        self.email = UserInterface.get_user_string("Enter the Email Address You Would like us to use to Contact you")
        self.registration_number = UserInterface.get_user_int(int)

    def notification(self, is_winner):
        is_winner = False
        if is_winner:
            print("You are Not Today's Luck Winner. Maybe Next Time!")
        else:
            print("Congratulations! You are Today's Lucky Winner!")
