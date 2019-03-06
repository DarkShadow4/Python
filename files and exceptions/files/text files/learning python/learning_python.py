filename = "learning_python.txt"

FileNotFoundError = IOError

try:
    with open(filename) as file:
        wtf = file.read()
        print wtf.rstrip()
except FileNotFoundError:
    with open(filename, "a") as file:
        file.write("FOOL")

try:
    with open(filename) as file:
        for line in file:
            print line.rstrip()
except FileNotFoundError:
    with open(filename, "a") as file:
        file.write("FOOL")

file_lines = []

try:
    with open(filename) as file:
        for line in file:
            file_lines.append(line.rstrip())
except FileNotFoundError:
    with open(filename, "a") as file:
        file.write("FOOL")
else:
    for line in file_lines:
        print line

file_lines = []

try:
    with open(filename) as file:
        for line in file:
            file_lines.append((line.rstrip()).replace("Python", "JavaScript"))
except FileNotFoundError:
    with open(filename, "a") as file:
        file.write("FOOL")
else:
    for line in file_lines:
        print line
