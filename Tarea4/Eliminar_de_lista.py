#   se requiere crear una funcion para eliminar elementos de una lista
#   los elementos solicitados deben ser eliminados de la lista (todos)
#   Crear una funcion que crea una lista
#   poner elementos que sean parte de la lista
#   poner elemento a eliminar de la lista
#   el resultado debe imprimir la nueva lista sin el elemento eliminado

def add_elements(add_to_list, eliminar):
    my_list = []
    
    for elemento_add in add_to_list:
        my_list.append(elemento_add)
    print("Input: ", "\n", my_list)

    my_new_list = [elemento_add for elemento_add in my_list if elemento_add != eliminar]
    print("Output: \n", my_new_list)

    # new_list = []
    # if elemento_add != eliminar:
    #     my_list.append(eliminar)
    # print(new_list)
    # print(my_list)


    # my_new_list = []
    # for elemento_remove in my_list:
    #     if eliminar in elemento_remove:
    #         my_new_list.remove(elemento_remove)
    
    # my_new_list = [elemento_add for elemento_add in my_list if elemento_add != eliminar]
    # print(my_new_list)

#   Prueba 1:
# add_elements([1,2,3,4,5,6,7,8,9],3)
#   Prueba 2:
# add_elements([1,2,3,3,3,6,7,8,9],3)
#   Prueba 3:
# add_elements(["gato","perro","loro","cocodrilo","mono"],"loro")
#   Prueba 4:
add_elements(["loro","perro","loro","cocodrilo","mono"],"loro")