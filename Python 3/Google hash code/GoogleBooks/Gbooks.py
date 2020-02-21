import statistics, sys

class Library(object):
    """docstring for Library."""
    def __init__(self, ID, n_books, signup_time, books_p_day, books, mean):
        super(Library, self).__init__()
        self.ID = ID
        self.n_books = n_books
        self.signup_time = signup_time
        self.books_p_day = books_p_day
        self.books = books
        self.mean = mean

    def potential(self, remaining_days):
        return(self.books_p_day*(remaining_days-self.signup_time))


def get_input(filename):
    books = {}
    libraries = []
    with open(filename, "r") as indata:
        B, L, D = indata.readline().split()
        B, L, D = int(B), int(L), int(D)
        book_values = [int(value) for value in indata.readline().split()]
        for bid in range(len(book_values)):
            books[bid] = book_values[bid]

        for ID in range(L):
            N, T, M = indata.readline().split()
            N, T, M = int(N), int(T), int(M)
            booksinlibrary = sorted([int(book) for book in indata.readline().split()], key=lambda book:books[book], reverse=True)
            libraries.append(Library(ID, N, T, M, booksinlibrary, statistics.mean([books[book] for book in booksinlibrary])))
    return(B, L, D, books, libraries)

filename = sys.argv[1]
# filename = "b_read_on.txt"
B, L, D, books, libraries = get_input(filename)

the_chosen_ones = {}
remaining = D
scanned_books = []
i = 0
done = False
while remaining > 0 and not done:
#######
    # library_potentials = {}
    # for library in libraries:
        # if library.ID not in the_chosen_ones.keys():
            # library_potential = library.books_p_day*(remaining-library.signup_time)
            # library_potentials[library.ID] = library_potential

    # for library in library_potentials.keys():
        # # values = [books[book] for book in books.keys()]
        # print("Library {0} needs {1} days to signup and is has a worth value of {2} with a mean book value of {3}".format(library, libraries[library].signup_time, library_potentials[library], libraries[library].mean))
    # remaining_libraries = [library for library in libraries if library.ID not in the_chosen_ones.keys() and library_potentials[library.ID] > 0]
    # remaining_libraries = sorted([library for library in remaining_libraries], key=lambda library:library.mean/(library_potentials[library.ID]*library.signup_time), reverse=True)
    libraries = sorted([library for library in libraries if library.potential(remaining) > 0], key=lambda library:library.mean/(library.potential(remaining)*library.signup_time), reverse=True)
##########
    # the_chosen_ones[libraries[i].ID] = [book for book in libraries[i].books[:library_potentials[libraries[i].ID]] if book not in scanned_books]
    # the_chosen_ones[libraries[0].ID] = [book for book in libraries[0].books[:libraries[0].potential(remaining)] if book not in scanned_books]
    # for book in the_chosen_ones[libraries[i].ID]:
    #     scanned_books.append(book)

    # the_chosen_ones[libraries[0].ID] = [book for book in libraries[0].books[:libraries[0].potential(remaining)] if book not in scanned_books]
    # for book in the_chosen_ones[libraries[i].ID]:
    #     scanned_books.append(book)
    if len(libraries) > 0:
        the_chosen_ones[libraries[0].ID] = []
        for book in libraries[0].books[:libraries[0].potential(remaining)]:
            if book not in scanned_books:
                the_chosen_ones[libraries[0].ID].append(book)
                scanned_books.append(book)
        remaining -= libraries[0].signup_time
        del libraries[0]
        i += 1
    else:
        done = True

#
# for lib in the_chosen_ones.keys():
#     print("Library {0} will scan the following books: ".format(lib), end="")
#     print(the_chosen_ones[lib])
file_sol = filename[:-4]+"_sol.txt"
with open(file_sol, "w+") as solution:
    line = "{0}".format(len(the_chosen_ones.keys()))
    solution.write(line+"\n")
    for library in the_chosen_ones.keys():
        if len(the_chosen_ones[library]) > 0:
            line = "{0} {1}".format(library, len(the_chosen_ones[library]))
            solution.write(line+"\n")
            line = ""
            for book in the_chosen_ones[library]:
                line = line + str(book) + " "
            solution.write(line+"\n")
