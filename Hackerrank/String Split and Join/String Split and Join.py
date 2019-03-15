def split_and_join(line):
    line = "-".join(line.split())
    return line

line = raw_input()
result = split_and_join(line)
print result
