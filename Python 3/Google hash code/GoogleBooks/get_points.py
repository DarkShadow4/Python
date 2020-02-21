import sys
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
            # libraries.append(Library(ID, N, T, M, booksinlibrary, statistics.mean([books[book] for book in booksinlibrary])))
    return(B, L, D, books, libraries)

def get_solution(solution_name):

    with open(filename, "r") as sol:
        libnum = int(sol.readline())
        books = []
        for i in range(libnum):
            library = sol.readline()
            books = books+[int(book) for book in sol.readline()]
    return (books)

filename = sys.argv[1]
solution_name = sys.argv[2]
# filename = "b_read_on.txt"
B, L, D, books, libraries = get_input(filename)
scanned_books = get_solution(solution_name)
points = 0
for book in scanned_books:
    points += books[book]
