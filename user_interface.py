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
            print("Invalid entry. Try again.")
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
        print(f"Registration Number: {contestant.registration_number} Full Name: {contestant.first_name} {contestant.last_name} Email: {contestant.email}")

    @staticmethod
    def display_sweepstakes_selection_menu(all_sweepstakes):
        print("list of on going Sweepstakes")

    @staticmethod
    def display_sweepstakes_menu_choices():
        print("Enter -1- to register in a sweepstakes.")
        print("Enter -2- to choose a winner. ")
        print("Enter -3- to view contestant information. ")
        print("Enter -4- to go back to the main menu. ")
        return

    @staticmethod
    def display_marketing_firm_menu_choices():
        print("Enter -1- to make a sweepstakes.")
        print("Enter -2- to select a sweepstakes. ")
        print("Enter -3- to change the marketing firm name. ")
        print("Enter -4- to go back to the main menu.")
        return

    @staticmethod
    def welcome_message():
        print("Welcome to the  devCodeCamp Sweepstakes Application.")
        print("Enter -1- to see the sweepstakes menu.")
        print("Enter -2- to see the marketing firm menu ")
        print("Enter -3- to close the application.")
        pass
