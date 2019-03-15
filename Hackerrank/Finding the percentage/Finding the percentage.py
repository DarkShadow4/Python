import math

n = input()
students = {}
for std in range(n):
    student = raw_input().split()
    name, scores = student[0], student[1:]
    scores = map(float, scores)
    students[name] = scores


for student, scores in students.items():
    scores = sum(scores)/len(scores)
    scores = "{0:.2f}".format(scores)
    students[student] = scores

who = raw_input()
print students[who]
