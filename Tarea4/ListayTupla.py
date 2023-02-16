#   Se debe crear un programa que funcione por medio de una funcion
#   La funcion debe recibir una secuencia de numeros separados por coma
#   se debe validar que sean numeros
#   si no son numeros, entonces da error, sino se continua
#   la secuencia de numeros debe ser agregado a una lista
#   al mismo tiempo la secuencia de numeros debe ser agregado a una tupla
#   el resultado debe presentar la secuencia de numeros como lista y como tupla

secuencia = input("Digite una secuencia de numeros separados por coma: \n")

def listatupla(secuencia):
    mylist = secuencia.split()
    print("Resultado:\n", "Lista: ", mylist)
    mytuple = tuple(mylist)
    print("Tupla: ", mytuple)


listatupla(secuencia)

#   Prueba 1:
# 1
#   Prueba 2:
# 1,2,3,4
#   Prueba 3:
# 50,6,7000