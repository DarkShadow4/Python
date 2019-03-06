filename = "Guest book.txt"
q = False

with open(filename, "a") as file:
    while q == False:
        try:
            username = raw_input("Enter your name please: ")
        except TypeError:
            pass
        else:
            if username != "q":
                file.write(username + "\n")
                print "Welcome,", username
            else:
                q = True
