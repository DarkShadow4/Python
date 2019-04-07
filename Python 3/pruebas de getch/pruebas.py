import getch

while True:
    print("se supone que espero a que pulses una tecla...")
    char = getch.getch()
    #char = input()
    pedir = any([char != "w", char != "W"])
    if pedir:
        print ("introduce otro")
    else:
        print (char),
