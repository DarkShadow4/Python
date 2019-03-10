import subprocess
programa = "'/media/eric/ERIC/Python/olimpiada/problema_palabras/problema-palabras.py'"
fichero_in = "input01.txt"
fichero_out = "salida_real"
fichero_generado = ">"+fichero_out
fichero_entradas = "<"+fichero_in
comando = " ".join(("pyhton", programa, fichero_entradas, fichero_generado))
# subprocess.run("python", fichero_entradas, fichero_generado)
# subprocess.call(comando)
print comando
fichero_a_comparar = "output01.txt"
comando = " ".join(("diff", fichero_out, fichero_a_comparar))
# subprocess.run("diff", fichero_out, fichero_a_comparar)
print comando
# subprocess.call(comando)
