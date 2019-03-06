"""Dumps numbers from 0 to 9 into the json file"""

import json

def json_dump_ej(filename):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    with open(filename, 'w') as file:
        json.dump(numbers, file)
