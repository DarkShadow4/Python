	
def generar_hangar():
	"""Funcion para generar el hangar tal y como aparecera siempre como minimo"""
	ubicaciones = []
	ubicaciones.append("T")
	for i in range(9):
		ubicaciones.append("o")
	ubicaciones.append("T")
	return ubicaciones

def get_torretas(ubicaciones):
	"""Funcion para recoger las torretas adicionales que hay en el hangar"""
	torretas_adicionales = 10
	
	while torretas_adicionales < 0 or torretas_adicionales > 4:
		torretas_adicionales = input("Numero de torretas adicionales: ")
	
	ubicacion_anterior = 0
	
	while torretas_adicionales > 0:
		if ubicacion_anterior is not 8:
			ubicacion = input("Ubicacion: ")
			if ubicacion%2 == 0:
				if ubicacion > ubicacion_anterior:
					if ubicaciones[ubicacion] == "o":
						ubicaciones[ubicacion] = "t"
						torretas_adicionales -= 1
				else:
					print "Ubicacion no valida"
			else:
				print "Ubicacion no valida"
			ubicacion_anterior = ubicacion
		else:
			print "Supondre que intentabas trolearme"
			repair = True
			ubicacion = 0
			while repair == True:
				ubicacion += 1
				if ubicacion%2 == 0:
					if ubicaciones[ubicacion] == "o":
						ubicaciones[ubicacion] = "t"
						torretas_adicionales -= 1
					else:
						repair = False

def encontrar_mejor_sitio(ubicaciones):
	"""Funcion no terminada, simplemente muestra algo si hay el maximo o no hay torretas adicionales"""
	torretas_adicionales = ubicaciones.count("t") # obtengo cuantas t (torretas adicionales) hay en ubicaciones
	if torretas_adicionales == 0:
		print "Posicion: 5"
	if torretas_adicionales == 4:
		print "Posicion: ",
		for i in range(len(ubicaciones)):
			if ubicaciones[i] == "o":
				print i, 
ubicaciones = generar_hangar()
get_torretas(ubicaciones)

print ubicaciones

encontrar_mejor_sitio(ubicaciones)
