transformations = {
    "LBR":"B",
    "LBS":"R",
    "RBL":"B",
    "SBL":"R",
    "SBS":"B",
    "LBL":"S"
}

def can_b_better(route):
    """Returns true if the route can be optimized"""
    i = 0
    while i+1 <= len(route):
        if route[i:i+3] in transformations.keys():
            return True
        i += 1
    return False

def optim_maze(route):
    """Function that gets the route and optimizes it"""
    while can_b_better(route):
        i = 0
        while i+3 <= len(route):
            if route[i:i+3] in transformations.keys():
                change=transformations[route[i:i+3]]
                print("Route: {0} and changes {1} for {2} and we get:".format(route, route[i:i+3], change), end="")
                route = route[0:i]+change+route[i+3:]
                print(route)
            else:
                i += 1
    return (route)



print(optim_maze("LBLLLBSBLLBSLL"))
