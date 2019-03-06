#### #### #### #### FILES #### #### #### ####

#### #### OPENING FILES #### ####

filename = "pi.txt"

#### EXAMPLE 1 ####

with open(filename) as Pi:
    pi_number = Pi.read()
    print pi_number.rstrip()

#### EXAMPLE 2 ####

with open(filename) as Pi:
    for line in Pi:
        print line.rstrip()

#### EXAMPLE 3 ####

with open(filename) as Pi:
    lines = Pi.readlines()

for line in lines:
    print line.rstrip()

#### EXAMPLE 4 ####

with open(filename) as Pi:
    lines = Pi.readlines()

    pi = ''
    for line in lines:
        pi += line.strip()
print pi
print len(pi)

#### #### WRITING FILES #### ####

filename = "testing.txt"

#### EXAMPLE 1 ####

with open(filename, 'w') as file:
    file.write("Python is sometimes so lovely.\n")

#### EXAMPLE 2 ####

with open(filename, "a") as file:
    file.write("I love the feeling of me being able to do what i want to do.\n")
