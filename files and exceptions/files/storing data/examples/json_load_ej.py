"""Loads the contents from the json file"""

import json

def json_load_ej(filename):
    with open(filename) as file:
        numbers = json.load(file)

    print numbers
