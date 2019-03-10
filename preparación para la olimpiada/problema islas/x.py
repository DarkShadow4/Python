base = 10
for i in reversed(range(base-1)):
    for x in reversed(range(i+1)):
        print "",
    print "*",
    print (base-(i+3)),
    for x in reversed(range(base-(i+3))):
        print " ",
    if i < (base-2):
        print "* ",
    else:
        print " ",
