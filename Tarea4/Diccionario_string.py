#   Ejercicio 2:
#   Crear una funcion con todas las apariciones de los caracteres en una palabra (string)
#   Crear una funcion que valide el input como una palabra
#   Si la validacion es incorrecta debe dar error (input debe ser una palabra)
#   Si la validacion es una palabra, entonces debe continuar
#   Agregar palabra en un diccionario
#   Diccionario debe contar todos los caracteres e imprimirlos en pantalla

def diccionario(input):
    if " " in input:
        print("Error... Palabra no debe contener espacios")
    else:  
        string_dict = {}
        for letra in input:
            string_dict[letra] = string_dict.get(letra,0) + 1
        print(string_dict)

#   Prueba 1:
diccionario("mamerto")
#   Prueba 2:
# diccionario("papa yon")
#   Prueba 3:
# diccionario(";alsidaneneo@#$$4;li")
#   Prueba 4:
# diccionario(";alsidane neo@#$$4;li")