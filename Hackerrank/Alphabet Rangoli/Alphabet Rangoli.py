import string
def print_rangoli(size):
    alpha = string.ascii_lowercase # string.ascii_lowercase devuelve todas las letras del código ascii que sean minúsculas

    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n]) # junta los carácteres del str alpha desde i hasta n con un guión
        L.append((s[::-1]+s[1:]).center(4*n-3, "-")) # añade a la lista de líneas la suma centrada del inverso del string s y s desde el segundo caracter el centrado lo hace siempre al
        # cuádruple de n restándole 3
    print('\n'.join(L[:0:-1]+L)) # imprime por pantalla la unión de los elementos de la lista de líneas con saltos de linea entre cada elemento
    # realmente imprime un string   

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
