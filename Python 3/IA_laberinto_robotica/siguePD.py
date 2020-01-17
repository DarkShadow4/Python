# I izquierda
# D derecha
# B atras
# S frente(Straight)

def gira(direccion):
    if direccion == "B":    # Por el programa y la forma de recorrer el laberinto
                            # para dar media vuelta gira dos veces a la izquierda
        trash = gira("I")
        trash = gira("I")
        return "B"

    if direccion == "D":
        pass # gira a la derecha
    elif direccion == "I":
        pass # gira a la izquierda

    return direccion # si es cualquier cosa que no sea media vuelta ("B") entonces lo devuelve tal cual

def siguePD(camino = []):
    if distancia("D") > umbralDcha): # Si no hay pared a la derecha
        camino.append(gira("D")) # gira a la derecha para seguir la pared derecha
    elif: # Si hay pared a la derecha
        if distancia("S") < umbralFrontal:  # Si hay pared delante (y a la derecha)
            if distancia("I") > umbralIzq:  # pero no a la izquierda
                camino.append(gira("I")) # gira a la izquierda
            else:                           # si la hay
                camino.append(gira("B")) # da media vuelta
        elif distancia("I") > umbralIzq: # si no hay pared delante pero sí a la derecha sigue para delante
            camino.append("S")           # pero comprueba si hay algún giro a la izquierda
