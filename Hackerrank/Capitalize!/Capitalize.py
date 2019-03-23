s = raw_input() # introduce el string
for x in s[:].split(): # separa las palabras del string
    s = s.replace(x, x.capitalize()) # modifica el string original cambiando cada palabra por la misma capitalizada
print s # imprime el output con dobles espacios en caso de haberlos( hackerrank eres un hijo de puta)
