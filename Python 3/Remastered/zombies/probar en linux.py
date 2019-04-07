import msvcrt, sys, datetime
while True:
    if msvcrt.kbhit():
        ch = msvcrt.getwch()
        if ch == 'q':
           sys.exit()
        else:
           print (ch, " Pressed at : ", datetime.datetime.now().time())
