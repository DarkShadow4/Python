x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
Coords = []
X = []
Y = []
Z = []
for i in range(x+1):
    for j in range(y+1):
        for h in range(z+1):
            X.append(i)
            Y.append(j)
            Z.append(h)
Coords = zip(X, Y, Z)
for i in range(len(Coords)):
    Coords[i] = list(Coords[i])

delete = []

for i in Coords:
    if sum(i) == n:
        delete.append(i)

for i in delete:
    del Coords[Coords.index(i)]
print Coords
