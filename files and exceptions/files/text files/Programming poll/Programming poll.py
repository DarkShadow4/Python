filename = "survey.txt"
q = False

with open(filename, "a") as file:
    while q == False:
        try:
            answer = raw_input("Why do you like programming?")
        except TypeError:
            pass
        else:
            if answer != "q":
                file.write(answer + "\n")
            else:
                q = True
