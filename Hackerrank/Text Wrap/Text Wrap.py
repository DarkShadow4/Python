import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

string, max_width = raw_input(), int(raw_input())
result = wrap(string, max_width)
print result
