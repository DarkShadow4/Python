import random
import datetime
random.seed()



def generar_apuesta():
	"""Funcion que genera una apuesta"""
	a = []
	while len(a) < 6:
		numero = random.randint(1, 49)
		if numero not in a:
			a.append(numero)
	return a

def mostrar_apuesta(apuestas, i):
	"""Funcion que muestra una apuesta"""
	print "apuesta", i+1, ":",
	for x in apuestas[i]:
		print x,
	print ""

tiempo_inicial = datetime.datetime.now()

apuestas = []

napuestas = input("Introduce numero de apuestas:")

for i in range(napuestas):
	a = generar_apuesta()
	apuestas.append(a)


for i in range(len(apuestas)):
	mostrar_apuesta(apuestas, i)


tiempo_final = datetime.datetime.now()
tiempo_total = tiempo_final - tiempo_inicial

print "Ha tardado", int(tiempo_total.total_seconds() * 1000), "milisegundos en realizar el proceso" # milliseconds
