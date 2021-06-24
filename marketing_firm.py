from sweepstakes import Sweepstakes
from user_interface import UserInterface


class MarketingFirm:

    def __init__(self):
        self.name = "name"
        self.sweepstakes_dictionary = ["Morgan & Morgan & Morgan ", "Real Fake Firms International"]

    def create_sweepstakes(self):
        new_sweepstakes = UserInterface.get_user_string("Enter name of the new sweepstakes")
        self.sweepstakes_dictionary.append(new_sweepstakes)

    def select_sweepstakes(self):
        (self=None):
        userInterface.display_sweepstakes_selection_menu()
        all_sweepstakes = userInterface.get_user_input_number("Select a sweepstake number")
        sweepStakes.Sweepstakes.sweepstakes_menu(self)
        pass

    def change_marketing_firm_name(self):
        self.name = UserInterface.get_user_string("Enter the name of your firm")

    def menu(self):
        UserInterface.display_marketing_firm_menu_choices()
        user_selection = UserInterface.get_user_int("Enter the number that corresponds with your choice")
        if user_selection == 1:
            MarketingFirm.create_sweepstakes("")
        elif user_selection == 2:
            self.select_sweepstakes()
        elif user_selection == 3:
            self.change_marketing_firm_name()
        else:
            pass
