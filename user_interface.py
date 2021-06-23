from marketing_firm import MarketingFirm
from sweepstakes import Sweepstakes


class UserInterface:
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_user_int(prompt):
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Enter a Number")
            return UserInterface.get_user_int(prompt)

    @staticmethod
    def get_user_string(prompt):
        user_input = input(prompt)
        return user_input

    @staticmethod
    def display_sweepstakes_info(sweepstakes):
        pass

    @staticmethod
    def display_contestant_info(contestant):
        print(
            f"Contestant Number: #{contestant.registration_number}: Full Name: {contestant.first_name} {contestant.last_name} Email: {contestant.email}")

    @staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        i = 1
        print("Which of these Sweepstakes would you like to you like to enter?:")
        for sweepstake in all_sweepstakes:
            print(f"{i}: {sweepstake.name}")

    @staticmethod
    def display_sweepstakes_menu_choices():
        print("Enter -1- to register In a Sweepstakes.")
        print("Enter -2- to choose a winner. ")
        print("Enter -3- to view contestant information. ")
        user_selection = UserInterface.get_user_int("Enter the number of your choice")
        if user_selection == 1:
            Sweepstakes.register_contestant()
        elif user_selection == 2:
            Sweepstakes.choose_winner()
        elif user_selection == 3:
            Sweepstakes.show_contestant()
        else:
            pass

    @staticmethod
    def display_marketing_firm_menu_choices():
        print("Enter -1- to make a sweepstakes.")
        print("Enter -2- to select a sweepstakes. ")
        print("Enter -3- to change the marketing firm name. ")
        user_selection = int(input("Type the Number Corresponding to your Selection Here:"))
        if user_selection == 1:
            MarketingFirm.create_sweepstakes()
        elif user_selection == 2:
            MarketingFirm.select_sweepstakes()
        elif user_selection == 3:
            MarketingFirm.change_marketing_firm_name()
        else:
            pass

    @staticmethod
    def welcome_message():
        print("Welcome to the  devCodeCamp Sweepstakes Application.")
        print("Enter -1- to see the sweepstakes menu.")
        print("Enter -2- to see the marketing firm menu ")
        user_selection = UserInterface.get_user_int("Enter the number of your choice")
        if user_selection == 1:
            UserInterface.display_marketing_firm_menu_choices()
        elif user_selection == 2:
            UserInterface.display_sweepstakes_menu_choices()
        else:
            pass
