from __future__ import print_function

def print_part_1(n, m):
    for i in range((n/2)):
        print( nothing.rjust(((m/2)-i*3)-1, hyphen), end="") # prints the -(...)-. part
        # print(((m/2)-(n-i))-((n/2)-(i+1)))
        for x in range(((m/2)-(n-i))-((n/2)-(i+1))): # prints the |.. part
            print( vbar.center(3, dot), end="")

        print( nothing.ljust(((m/2)-i*3)-1, hyphen)) # prints the .-(...)-part

def print_part_2(n, m):
    print( "WELCOME".center(m, hyphen))

def print_part_3(n, m):
    for i in reversed(range((n/2))):
        print( nothing.rjust(((m/2)-i*3)-1, hyphen), end="") # prints the -(...)-. part
        # print(((m/2)-(n-i))-((n/2)-(i+1)))
        for x in range(((m/2)-(n-i))-((n/2)-(i+1))): # prints the |.. part
            print( vbar.center(3, dot), end="")

        print( nothing.ljust(((m/2)-i*3)-1, hyphen)) # prints the .-(...)-part

nothing = ""
dot = '.'
hyphen = '-'
vbar = '|'
n, m = raw_input().split()
n, m = int(n), int(m)

print_part_1(n, m)
print_part_2(n, m)
print_part_3(n, m)
