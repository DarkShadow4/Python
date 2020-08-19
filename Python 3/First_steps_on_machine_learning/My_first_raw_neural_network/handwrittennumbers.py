import numpy

def sig(z): # this is just a placeholder
    return (1/(1+numpy.e**(-z)))

def get_gradient_descent(w, a, bias):
    for 

def backpropagation(w, a, bias):
    pass


##################################
# weights
w=[
    [
        [1, 2, 4],
        [3, 1, 7]
    ],
    [
        [4, 6],
        [9.5, 4.005]
    ]
]
a = [
    [1, 0.5, 0.7],
    [0, 0],
    [0, 0]
]
bias = [
    [],
    [4, 2],
    [3, 7]
]
##################################

for L in range(1, len(a)):
    for j in range(len(a[L])):
        z = 0
        print("Layer {0}; neuron {1}".format(L, j))
        for w_jk, a_k in zip(w[L-1][j], a[L-1]):

            print(w_jk, end=" ")
            print(a_k)
            z += w_jk*a_k
        z += bias[L][j]
        print(z)
        a[L][j] = sig(z)
        print(a[L][j])
print(a)
expected = [0.5, 0.73]
last_layer = len(a)-1


# cost of the example
cost = sum((out-expected_out)**2 for out, expected_out in zip(a[last_layer], expected))/last_layer
print(cost)
