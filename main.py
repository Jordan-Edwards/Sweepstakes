from marketing_firm import MarketingFirm
from sweepstakes import Sweepstakes
from user_interface import UserInterface

UserInterface.welcome_message()
user_selection = UserInterface.get_user_int("Enter the number that corresponds with your choice.")
if user_selection == 1:
    MarketingFirm.menu("")
elif user_selection == 2:
    Sweepstakes.menu("")
else:
    pass