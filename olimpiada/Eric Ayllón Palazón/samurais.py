# Eric Ayllon Palazon
import random
def get_potencias():
	"""Funcion para obtener las potencias"""
	potencias = [0]
	while sum(potencias) != 30:
		potencias = raw_input("Introdice potencia de los samurai:").split() # cojo como una cadena de texto los numeros y lo divido en los numeros
		for pot in range(len(potencias)):
			potencias[pot] = int(potencias[pot])
		if sum(potencias) != 30: #si la suma de todos los elementos(potencias) es 30, no repite el input
			print "Error no suma 30 la potencia total"
	print "Perfecto, equipo completado"
	return potencias

def batalla(potencias1, potencias2):
	"""Funcion que simula la batalla"""
	samurai = random.randint(0, 6) #obtengo el primer samurai aleatoriamente
	print "Empezamos con el samurai", samurai+1
	while potencias1.count(0) < 4 and potencias2.count(0) < 4:
		print "Samurai", samurai+1,
		if potencias1[samurai] > potencias2[samurai]: #compruebo quien gana cada ronda
			print "Gana jugador 1", potencias1[samurai], "vs", potencias2[samurai]
			potencias2[samurai] = 0
		elif potencias1[samurai] < potencias2[samurai]:
			print "Gana jugador 2", potencias1[samurai], "vs", potencias2[samurai]
			potencias1[samurai] = 0
		else:
			print "Empate, ambos samurais mueren", potencias1[samurai], "vs", potencias2[samurai]
			potencias1[samurai] = 0
			potencias2[samurai] = 0
		if samurai == 6: #aqui evito que se salga del limite del indice
			samurai = 0
		else:
			samurai += 1
	if potencias1.count(0) >= 4: #devuelvo el resultado de la guerra
		return str("El equipo 2 vence, el jugador 1 tiene " + str(potencias1.count(0)) + " bajas")
	elif potencias2.count(0) >= 4:
		return str("El equipo 1 vence, el jugador 2 tiene " + str(potencias2.count(0)) + " bajas")
	else:
		return str("Ambos equipos pierden demasiados samurais y no pueden seguir combatiendo")


random.seed() #establezco la semilla de los random con la por defecto (el tiempo del sistemaS)

print "Equipo 1"
potencias1 = get_potencias()
print "Equipo 2"
potencias2 = get_potencias()
resultado = batalla(potencias1, potencias2)
print resultado
