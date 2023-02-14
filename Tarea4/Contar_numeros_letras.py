#   Ejercicio 1:
#   Se necesita una funcion que imprima en pantalla la cantidad de letras, numeros y caracteres especiales para un STRING
#   Se debe definir un input como un string
#   Se debe verificar si la palabra contiene espacios (asi se define que no es una sola palabra)
#   Si es una palabra, se continua con la funcion
#   La funcion cuenta la cantidad de letras
#   La funcion cuenta la cantidad de numeros
#   La funcion cuenta la cantidad de caracteres especiales
#   Pruebas en palabras llamando a la funcion


def cuenta(input):
    
    if " " in input:
        print("Error... Palabra no debe contener espacios")
    else:

        letras = 0
        numeros = 0
        caracteres = 0

        for char in input:
            if char.isalpha():
                letras += 1
            elif char.isdigit():
                numeros += 1
            else:
                caracteres += 1

        print("Cantidad de letras: ", letras)
        print("Cantidad de numeros: ", numeros)
        print("Cantidad de caracteres especiales: ", caracteres)

#   prueba 1:
cuenta("Pyth0n35l0M4x$!*0")
#   prueba 2:
# cuenta("l;a;kjdi)(& )")
#   prueba 3:
# cuenta("l;a;kjdi)(&)")
#   prueba 4:
# cuenta("Pyth0n35l 0M4x$!*0")
