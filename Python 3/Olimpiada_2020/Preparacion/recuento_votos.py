import sys

def get_points(papeleta, candidates, p, n):
    papeleta = papeleta.split()
    papeleta = [int(points) for points in papeleta]

    if sorted(papeleta) == [i for i in range(1,n+1)]:
        candidate_names = [name for name in candidates.keys()]
        for c in range(n):
            candidates[candidate_names[papeleta[c]-1]] += n-(c+1)   # its c+1 so it goes from 1 to n
    else:                                       # and so the last one gets 0
        print("Papeleta no válida")

def get_the_chosen_ones(candidates, p): # de momento no lo hace en orden alfabético si hay empate
    the_chosen_ones = []
    for chosen_number in range(p):
        found = False
        for key, value in sorted(candidates.items(), key=lambda x:x[0]): # as I sort the tuple alphabetically, i do not need to worry about sorting
                                                                         # a stalemate case
            if value == max(candidates.values()) and not found:
                the_chosen_ones.append(key)
                found = True
                del candidates[key]
    return(the_chosen_ones)

filename = sys.argv[1] # sys.argv[0] would be the name of this script
with open(filename, "r") as input_file:
    Id=input_file.readline().strip()
    p=int(input_file.readline().strip()) # " string ".strip() cuts the string from each side in order to erase white spaces
    n=int(input_file.readline().strip()) # so " string ".strip() would result in "string"
    candidates = {}
    for candidate in range(n):
        candidates[input_file.readline().strip()] = 0

    for line in input_file.readlines():
        line.strip()
        get_points(line, candidates, p, n)
        # c = 0
        # for candidate in candidates.keys():
        #     candidates[candidate] += line_points[c] # I add the points of the
        #     c += 1                                  # line to the points before
        #                                             # this line for each candidate

if sum(candidates.values()) == 0:
    print("VOTACION ANULADA")
else:
    the_chosen_ones = get_the_chosen_ones(candidates, p)
    for candidate in the_chosen_ones:
        print(candidate)
