def count_substring(string, sub_string):
    occurrences = 0
    for c in range(len(string)):
        if string[c:c+len(sub_string)] == sub_string:
            occurrences += 1
    return occurrences

string = raw_input().strip()
sub_string = raw_input().strip()
count = count_substring(string, sub_string)
print count
