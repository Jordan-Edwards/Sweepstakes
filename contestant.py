import user_interface


class Contestant:
    def __init__(self, fname, lname, email, registration_number):
        self.key = {
            "first_name": fname,
            "last_name": lname,
            "email": email,
            "reg_num": registration_number,
        }

    def notify_winner_status(self, notify_winner_status):
        notify_winner_status = False
        if notify_winner_status:
            pass
        else:
            pass
