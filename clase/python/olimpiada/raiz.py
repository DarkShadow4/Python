number = input("Enter number:")
# root = ""
# processing_number = str(number)

def get_step():
    precision = input("Enter the precision of the result: ")
    step = float(1)
    for i in range(precision):
        step = step/10
    return step

def find_root(number, step):
    for i in range(0, len(number)/2, step):
        if i*i == number:
            root = i
    return root

print find_root(str(number), get_step())

# Get precision
num = 3
step = get_step()
root = ""
for i in range(0, int(1/step)):
    root = str(i*step)
    for i in range((num+2)-len(str(i*step))):
        root = root+"0"
    print root
