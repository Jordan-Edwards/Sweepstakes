
class Contestant:
    def __init__(self, fname, lname, email, registration_number):
        self.key = {
            "first_name": fname,
            "last_name": lname,
            "email": email,
            "reg_num": registration_number,
            "winner_status": False
        }

    def notify_winner_status(self, winner_posted):
        if winner_posted['winner_status']:
            print(f"{winner_posted.key['fname']} {winner_posted['lname']}!"
                  f"WINNER WINNER CHICKEN DINNER! YOU HAVE WON!")
        else:
            print(f"{winner_posted.key['fname']} {winner_posted['lname']}"
                  f"So....there's no easy way to say this. You didn't win. But hey, there's always next time.")
