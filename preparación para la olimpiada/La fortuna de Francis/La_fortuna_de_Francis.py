def preparar_matricula(matricula, finalidad = 1):
    if finalidad == 1:
        numeros = matricula[:-3]
        letras = matricula[-3::]
        matricula = letras+numeros
        return matricula
    else:
        numeros = matricula[-4::]
        letras = matricula[:3]
        matricula = numeros+letras
        return matricula

n = input()
matriculas = []
for i in range(n):
    matricula = raw_input()
    matricula = preparar_matricula(matricula, 1)
    matriculas.append(matricula)

matriculas.sort()
matricula = preparar_matricula(matriculas[0], 2)
print matricula
