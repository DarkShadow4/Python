from users import User

class Privileges(object):
    """A simple class to store the privileges of the admin.py"""
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print privilege

class Admin(User):
    """A class trying to represent a user with admin privileges."""
    def __init__(self, first_name, last_name, sex, adress, email, privileges):
        super(Admin, self).__init__(first_name, last_name, sex, adress, email)
        self.privileges = Privileges(privileges)
