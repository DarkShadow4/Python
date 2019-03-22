from __future__ import print_function
n = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(n):
    line = []
    for j in range(n-i):
        # print(alphabet[n-(i+1)], end="-")
        line.append("{0!s:-<{width}}".format(alphabet[n-(j+1)], width = 2))
    line = "".join(line)
    print (line.center(((2*n)+((2*(n-1))-1))), "-")
