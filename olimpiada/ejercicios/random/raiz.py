number = input("Enter number:")
precision = input("Enter the precision of the result: ")


def get_step(precision):
    step = float(1)
    for i in range(precision):
        step = step/10
    return step

def find_root(number, precision, step):
    number = int(number)
    root = "Root not found"
    pasos = 0
    for i in range(0, int((number)/step)):
        if root == "Root not found":
            pasos += 1
        if round((i*step)*(i*step)) == number:
            root = i*step
    root = str(root)
    for i in range((precision+2)-len(str(i*step))):
        root = root+"0"
    print pasos
    return root

print find_root(str(number), precision, get_step(precision))
# Get precision
# num = 3
# print get_step(0)
# root = ""
# for i in range(0, int(1/step)):
#     root = str(i*step)
    # for i in range((num+2)-len(str(i*step))):
    #     root = root+"0"
    # print root
