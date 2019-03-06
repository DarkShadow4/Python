"""Dumps the username into the json file"""

import json

def ask_username(filename):
    username = raw_input("Whats your name? ")

    with open(filename, "w") as file:
        json.dump(username, file)
        print "We'll remember you when you come back,", username + "!"
