import __builtin__

try:
    number1 = input("Enter a number: ")
except NameError:
    print "That's not a number, you fool"
else:
    print "thx"
try:
    number2 = input("Enter another number: ")
except NameError:
    print "That's not a number, you fool"
else:
    print "thx"
