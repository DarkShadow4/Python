"""A class thet is made to represent users"""

class User(object):
    """A class representing a user."""

    def __init__(self, first_name, last_name, sex, adress, email):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.adress = adress
        self.email = email

    def describe(self):
        """Gives the info about the user"""
        print self.first_name.title(), self.last_name.title(), "lives in", self.adress, "and his email is:", self.email

    def greet(self):
        """Greets the user"""
        print "Welcome,", self.first_name.title()
