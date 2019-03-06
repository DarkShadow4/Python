import sys
while sys.stdin:
    n = input()
    palabra1 = raw_input()
    palabra2 = raw_input()

    if (palabra1.replace("?", "a") < palabra2.replace("?", "z")):
        print "si"
    else:
        print "no"
