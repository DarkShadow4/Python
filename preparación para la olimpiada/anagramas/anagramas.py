def make_words_the_same(w):
    w.lower()
    w = list(w)
    w.sort()
    str(w)
    return w

r = "s"
while r == "s":
    p1 = raw_input("Introduce palabra 1: ")
    p2 = raw_input("Introduce palabra 2: ")
    pn1 = make_words_the_same(p1)
    pn2 = make_words_the_same(p2)
    if  pn1 == pn2:
        print p1, "y", p2, "forman un anagrama"
    else:
        print p1, "y", p2, "no forman un anagrama"
    r = raw_input("Desea introducir otras dos palabras? ").lower()
