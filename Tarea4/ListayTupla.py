#   Se debe crear un programa que funcione por medio de una funcion
#   La funcion debe recibir una secuencia de numeros separados por coma
#   se debe validar que sean numeros
#   si no son numeros, entonces da error, sino se continua
#   la secuencia de numeros debe ser agregado a una lista
#   al mismo tiempo la secuencia de numeros debe ser agregado a una tupla
#   el resultado debe presentar la secuencia de numeros como lista y como tupla

secuencia = input("Digite una secuencia de numeros separados por coma: \n")


# def listatupla(secuencia):
    
mylist = []
for numero in secuencia:
    mylist.append(numero)
my_new_list = [numero for numero in mylist if numero != ","]
print("Resultado:\n", "Lista: ", my_new_list)

mytuple = tuple(my_new_list)
print("Tupla: ", mytuple)