b = input()
char = '+'
for i in range(base):
    print "{0!s:1^{base}}".format(char*(i+1), base=b)
