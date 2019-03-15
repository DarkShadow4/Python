N = input()
students = []
for i in range(N):
    student = ()
    name = raw_input()
    grade = input()
    student = (name, grade)
    students.append(student)
students = sorted(students, key = lambda x:x[1], reverse = False)
i = 0
lowest_grade = students[0][1]
second_lowest_grade = lowest_grade
while second_lowest_grade == lowest_grade:
    i += 1
    second_lowest_grade = students[i][1]

dumb_students = []
for student in students:
    if student[1] == second_lowest_grade:
        dumb_students.append(student[0])

dumb_students.sort()
for student in dumb_students:
    print student
