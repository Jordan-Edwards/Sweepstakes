from user_interface import UserInterface


class Contestant:
    def __init__(self):
        self.first_name = UserInterface.get_user_string("Enter your first name")
        self.last_name = UserInterface.get_user_string("Enter your last name")
        self.email = UserInterface.get_user_string("Enter your preferred email address")
        self.registration_number = 0

    def notify_winner_status(self, is_winner):
        is_winner = False
        if is_winner == False:
            pass
        else:
            pass
