def make_words_the_same(w):
    w.lower() # pongo en minúsculas todos los caracteres de la palabra
    w = list(w) # transformo la palabra en una lista de caracteres para poder ordenarlos
    w.sort() # ordeno los caracteres por orden alfabético
    return w #devuelvo la lista ya procesada

r = "s"
while r == "s":
    p1 = raw_input("Introduce palabra 1: ")
    p2 = raw_input("Introduce palabra 2: ")
    pn1 = make_words_the_same(p1) #guardo la lista en una variable nueva ya que no me interesa perder la palabra
    pn2 = make_words_the_same(p2) #guardo la lista en una variable nueva ya que no me interesa perder la palabra
    if  pn1 == pn2: #comparo si ambas listas son exactamente iguales
        print p1, "y", p2, "forman un anagrama"
    else:
        print p1, "y", p2, "no forman un anagrama"
    r = raw_input("Desea introducir otras dos palabras? ").lower() # este detalle es simplemente para que si se introduce s en mayuscula también lo reconozca
