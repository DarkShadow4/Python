s = raw_input()

def has_alnum(s):
    return any(c.isalnum() for c in s)

def has_alpha(s):
    return any(c.isalpha() for c in s)

def has_digits(s):
    return any(c.isdigit() for c in s)

def has_lower(s):
    return any(c.islower() for c in s)

def has_upper(s):
    return any(c.isupper() for c in s)

print has_alnum(s)
print has_alpha(s)
print has_digits(s)
print has_lower(s)
print has_upper(s)
