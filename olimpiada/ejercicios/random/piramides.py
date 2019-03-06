def get_base():
	"""Funcion para obtener la anchura de la base de la piramide"""
	base = input("Introduzca anchura de la base: ")
	return base

def get_forma():
	"""Funcion para obtener la direccion de la piramide"""
	direccion = raw_input("Normal o invertida?(n/i): ")
	forma = raw_input("Rellena o hueca?(r/h): ")
	return direccion, forma

def dibujar_normal_relleno(base):
	"""Funcion que dibuja la piramide normal hueca"""
	for i in reversed(range(base)):
		for x in range (i):
			print "",
		for x in range(base-i):
			print "*",
		print ""

def dibujar_invertida_relleno(base):
	"""Funcion que dibuja la piramide invertida rellena"""
	for i in range(base):
		for x in range (i):
			print "",
		for x in range(base-i):
			print "*",
		print ""

def dibujar_invertida_hueca(base):
	"""Funcion que dibuja la piramide invertida hueca"""
	for i in range(base):
			print "*",
	print ""
	for i in range(base-1):
		for x in range(i+1):
			print "",
		print "*",
		for x in range(base-(i+3)):
			print " ",
		if i < (base-2):
			print "*"
		else:
			print ""

def dibujar_normal_hueca(base):
	"""Funcion que dibuja la piramide normal hueca"""
	for i in reversed(range(base-1)):
		for x in reversed(range(i+1)):
			print "",
		print "*",
		for x in reversed(range(base-(i+3))):
			print " ",
		if i < (base-2):
			print "*"
		else:
			print ""
	for i in range(base):
		print "*",


def dibujar_piramide(base, direccion, forma):
	"""Funcion que dibuja la piramide"""
	if forma == "r":
		if direccion == "i":
			dibujar_invertida_relleno(base)
		else:
			dibujar_normal_relleno(base)
	else:
		if direccion == "i":
			dibujar_invertida_hueca(base)
		else:
			dibujar_normal_hueca(base)

def pedir_datos():
	"""Funcion que pide los datos para la piramide"""
	base = get_base()
	direccion, forma = get_forma()
	return base, direccion, forma

base, direccion, forma = pedir_datos()
dibujar_piramide(base, direccion, forma)
