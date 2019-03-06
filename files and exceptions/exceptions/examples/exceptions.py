#### #### #### #### EXCEPTIONS #### #### #### ####

#### #### COMMON EXCEPTION OBJECTS #### ####

# ZeroDivisionError
# FileNotFound

#### #### USING TRY-EXCEPT BLOCKS #### ####

#### EXAMPLE 1 (TRY-EXCEPT) ####

try:
    print(5/0)
except ZeroDivisionError:
    print "infinite"

#### EXAMPLE 2 (TRY-EXCEPT-ELSE) ####

print "Give me two numbers, and I'll divide them."
print "Enter 'q' to quit."

while True:
    n1 = raw_input("\nFirst number: ")
    if n1 == 'q':
        break
    n2 = raw_input("\nSecond number: ")
    if n2 == 'q':
        break
    try:
        answer = int(n1)/int(n2)
    except ZeroDivisionError:
        print "something divided by zero is infinite"
    else:
        print answer

#### EXAMPLE 3 (ANALYZING TEXT) ####

filename = 'suposed_book_one.txt'
try:
    with open(filename) as file:
        contents = file.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

#### EXAMPLE 4 (WORKING WITH MULTIPLE FILES) ####

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

filenames = ['suposed_book_one.txt', 'suposed_book_two.txt', 'suposed_book_five.txt', 'suposed_book_three.txt', 'suposed_book_four.txt']

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError as error_type:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

for filename in filenames:
    count_words(filename)

#### EXAMPLE 5 (FAILING SILENTLY) ####

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError
filenames = ['suposed_book_one.txt', 'suposed_book_two.txt', 'suposed_book_five.txt', 'suposed_book_three.txt', 'suposed_book_four.txt']

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

for filename in filenames:
    count_words(filename)
