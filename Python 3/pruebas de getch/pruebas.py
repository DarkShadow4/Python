import getch

while True:
    char = getch.getch()
    pedir = any([char != "w", char != "W"])
    if pedir:
        print "introduce otro"
    print char,
