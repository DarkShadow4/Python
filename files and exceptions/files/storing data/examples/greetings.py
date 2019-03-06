"""Loads the username from the json file"""

import json

def greet_user(filename):
    with open(filename) as file:
        username = json.load(file)
        print "Welcome back,", username + "!"
