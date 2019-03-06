filename = "username.txt"
username = raw_input("What's your name? ")
with open(filename, "w") as file:
    file.write(username)
