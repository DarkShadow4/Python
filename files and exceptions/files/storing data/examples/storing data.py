#### #### #### #### STORING DATA #### #### #### ####

#### #### USING JSON FILES #### ####

import json

# NOTE: The JSON (JavaScript Object Notation) format was originally developed for JavaScript.
# However, it has since become a common format used by many languages, including Python.

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

#### EXAMPLE 1 (DUMPING TO AND LOADING FROM JSON FILES) ####

import json_dump_ej
import json_load_ej

filename = "numbers.json"

json_dump_ej.json_dump_ej(filename)
json_load_ej.json_load_ej(filename)

#### EXAMPLE 2 ("Remember and greet me")####

import greetings
import remember_me

filename = "username.json"

remember_me.ask_username(filename)
greetings.greet_user(filename)

#### EXAMPLE 3 (a mix of the two programs in example 2)####

filename = "username.json"

try:
    with open(filename) as file:
        username = json.load(file)
except FileNotFoundError:
    username = raw_input("what's your name?")
    with open(filename, "w") as file:
        json.dump(username, file)
        print "We'll remember you next time you enter here,", username
else:
    print "Welcome back,", username + "!"
