n = input()
A = []
for a in raw_input().split():
    A.append(int(a))
A.sort(reverse = True)
a = A[0]
i = 0
while a == max(A) and i < len(A):
    i += 1
    if i < len(A):
        a = A[i]

print a
