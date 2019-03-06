def get_platos_y_dinero():
    """Funcion que obtiene el numero de platos y el dienro a gastar"""
    platos = input("Cuantos platos se sirven hoy? ")
    dinero_disponible = input("Cuanto dinero va a gastar?: ")
    return platos, dinero_disponible

prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512] # creo una lista con los precios para luego usarla en el bucle principal de este programa

platos, dinero_disponible = get_platos_y_dinero()
total_platos = 0
for i in reversed(prices[0:platos]): # No preocupa que el programa se pase del indice de la lista de precios pues no va a dar ningun traceback error
    while dinero_disponible/i > 0:
        total_platos += dinero_disponible/i
        dinero_disponible -= i*(dinero_disponible/i)

print "Numero de platos:", total_platos
