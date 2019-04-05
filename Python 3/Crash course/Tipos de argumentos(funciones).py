def funcion1(parametro1="Dato 1", parametro2="Dato 2"):
    print "Parametro 1:", parametro1
    print "Parametro 2:", parametro2

# def funcion2(parametro1, parametro2):
#     print "Parametro 1:", parametro1
#     print "Parametro 2:", parametro2

argumento1 = "Dato 1"
argumento2 = "Dato 2"

# Positional arguments
print "Positional arguments"
funcion1(argumento1, argumento2)
# Keyword arguments
print "Keyword arguments"
funcion1(parametro2=argumento2, parametro1=argumento1)
# Default values
print "Default values"
funcion1()
