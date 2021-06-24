from sweepstakes import Sweepstakes
from user_interface import UserInterface


class MarketingFirm:

    def __init__(self):
        self.name = "name"
        sweepstakes_dictionary = []

    def create_sweepstakes(self):
        MarketingFirm.name = UserInterface.get_user_string("What is the Name of the new Sweepstake?")
        MarketingFirm.sweepstakes_dictionary.append(self.name)
        MarketingFirm.menu(self)

    def select_sweepstakes(self):
        UserInterface.display_sweepstakes_selection_menu(self)
        all_sweepstakes = UserInterface.get_user_int("Select a sweepstake number")
        U.sweepstakes_menu(all_sweepstakes)
        return all_sweepstakes

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
